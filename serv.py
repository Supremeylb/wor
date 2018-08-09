import errno
import os
import signal
import socket

HOST, PORT = 'localhost', 8080
BACKLOG = 5


def grim_zom():
    while True:
        try:
            pid, status = os.waitpid(
                -1,  # wait for child process
                WNOHANG
            )

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(BACKLOG)
print 'Serving HTTP on port %s ...' % PORT
signal.signal(signal.SIGCHLD, grim_zom)


while True:
    try:
        client_connection, client_address = listen_socket.accept()
    except IOError as e:
        code, msg = e.args
        if code == errno.EINTR:
            continue
        else:
            raise
    pid = os.fork()
    if pid == 0:  # in child process
        listen_socket.close()
        data = client_connection.recv(1024)
        print data
        http_response = """\
                            HTTP/1.1 200 OK                  
                            Hello, World!
                            """
        client_connection.sendall(http_response)
        client_connection.close()
        os._exit(0)
    else:
        # in parent process
        client_connection.close()
