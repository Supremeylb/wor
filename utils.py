import json
import traceback


def save_file(file_path, content, log):
    try:
        with open(file_path, "w") as f:
            json.dump(content, f)
    except Exception as e:
        log.error("error in save_configs:%s" % traceback.format_exc())


def read_file(file_path, log):
    content = None
    try:
        with open(file_path, "r") as read_f:
            content = json.load(read_f)
    except Exception as e:
        log.error("error in save_configs:%s" % traceback.format_exc())
    return content
