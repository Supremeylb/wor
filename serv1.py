import socket
from select import select

import queue

input_list = []
output_list = []
message_queue = {}
if __name__ == '__main__':
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServer.bind(('127.0.0.1', 9999))
    socketServer.listen(5)
    socketServer.setblocking(0)
    input_list.append(socketServer)

    while True:
        w_list, r_list, e_list = select(input_list, output_list, input_list)
        for obj in input_list:
            if obj == socketServer:
                conn, addr = socketServer.accept()
                print("Client{0} connected".format(addr))
                input_list.append(conn)
                message_queue[conn] = queue.Queue()
            else:
                try:
                    data = obj.recv(1024)
                    if data:
                        print("received {0} from client {1}".format(data.decode(), addr))
                        message_queue[obj].put(data)
                        if obj not in output_list:
                            output_list.append(obj)
                except Exception as e:
                    input_list.remove(obj)
                    del message_queue[obj]
                    print("\n[input] Client  {0} disconnected".format(addr))
        for sendobj in output_list:
            try:
                if not message_queue[sendobj].empty():
                    send_data = message_queue[sendobj].get()
                    sendobj.sendall(send_data)
                else:
                    output_list.remove(sendobj)

            except Exception as e:
                del message_queue[sendobj]
                output_list.remove(sendobj)
                print("\n[output] Client  {0} disconnected".format(addr))
