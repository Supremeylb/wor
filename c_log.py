import logging
import logging.handlers
import os


def init_log(handle_name, file_name="", debug=False, rotate="size", count=5):
    """
    @param rotate: Log file rotate by 'date' or 'size'.
    """
    create_file = True
    log = HandyLog(create_file, handle_name, file_name,
                     debug, rotate, count=count)
    return log


class HandyLog(object):

    def __init__(self, create_file, handle_name, file_name="", debug=False, rotate="size", level=logging.DEBUG,
                 count=30):
        # self.records = []
        self.record_time = 0
        if not create_file:
            self.log = logging.getLogger(name=handle_name)
        else:
            self.log = logging.getLogger(name=handle_name)
            self.level = level
            if not file_name:
                file_name = handle_name
            logfile = os.path.join(
                os.getcwd(), "%s.log" % file_name.lower())
            path, f = os.path.split(logfile)
            if not os.path.exists(path):
                os.makedirs(path)
            formatter = logging.Formatter(
                '%(asctime)s,%(msecs)03d %(levelname).1s %(thread).4s %(message)s', "%y-%m%d %H:%M:%S")

            if not self.log.handlers:
                if rotate is False:
                    handle = logging.FileHandler(logfile)
                    handle.setFormatter(formatter)
                    self.log.addHandler(handle)
                else:
                    if rotate == 'size':
                        rotate_handle = logging.handlers.RotatingFileHandler(
                            logfile, maxBytes=1024 * 1024 * 10, backupCount=count, encoding="utf-8")
                    elif rotate == 'date':
                        rotate_handle = logging.handlers.TimedRotatingFileHandler(
                            logfile, 'midnight', backupCount=count, encoding="utf-8")
                    else:
                        rotate_handle = logging.handlers.RotatingFileHandler(
                            logfile, maxBytes=1024 * 1024 * 10, backupCount=count, encoding="utf-8")
                    rotate_handle.setFormatter(formatter)
                    self.log.addHandler(rotate_handle)
                if debug:
                    ch = logging.StreamHandler()
                    ch.setFormatter(formatter)
                    self.log.addHandler(ch)
                    self.log.setLevel(logging.DEBUG)
                else:
                    self.log.setLevel(logging.INFO)

    def debug(self, log):
        try:
            self.log.debug(log)
        except:
            self.log.exception("error: ")

    def info(self, log):
        try:
            self.log.info(log)
        except:
            self.log.exception("info: ")

    def warning(self, log):
        try:
            self.log.warning(log)
        except:
            self.log.exception("error: ")

    def error(self, log):
        try:
            self.log.error("\033[1;31m\n%s\n\033[0m" % log)
        except:
            self.log.exception("error: ")
