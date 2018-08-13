# -*-coding=UTF-8-*-
"""
Bryan
write on 09/08/2018
you can seek it by html dom or base on url
<div class="widget-pagelink-download-inner bbcle-download-linkparent-extension-http://www.bbc.co.uk/programmes/p02pc9tn/episodes/downloads"><a class="download bbcle-download-extension-http://www.bbc.co.uk/programmes/p02pc9tn/episodes/downloads" href="http://www.bbc.co.uk/programmes/p02pc9tn/episodes/downloads">6 Minute English</a></div>
<a class="download bbcle-download-extension-pdf" href="http://downloads.bbc.co.uk/learningenglish/features/6min/180719_6min_english_technochauvinism.pdf"><span data-i18n-message-id="Download PDF" class="not-translated _bbcle_translate_wrapper" lang="en">Download PDF</span></a>

<div class="widget-pagelink-download-inner bbcle-download-linkparent-extension-pdf"><a class="download bbcle-download-extension-pdf" href="http://downloads.bbc.co.uk/learningenglish/features/6min/180719_6min_english_technochauvinism.pdf"><span data-i18n-message-id="Download PDF" class="not-translated _bbcle_translate_wrapper" lang="en">Download PDF</span></a></div>

<div class="widget-pagelink-download-inner bbcle-download-linkparent-extension-mp3"><a class="download bbcle-download-extension-mp3" href="http://downloads.bbc.co.uk/learningenglish/features/6min/180719_6min_english_technochauvinism_download.mp3"><span data-i18n-message-id="Download Audio" class="not-translated _bbcle_translate_wrapper" lang="en">Download Audio</span></a></div>
questions listed below:
"""

import hashlib
import os
import subprocess
import time
import urllib
from datetime import datetime

from bs4 import BeautifulSoup

from c_log import init_log

log = init_log("GetBBC")

base_url = "http://www.bbc.co.uk/learningenglish/english/features/6-minute-english/ep-"
html = "<div class='widget-pagelink-download-inner bbcle-download-linkparent-extension-mp3'><a class='download bbcle-download-extension-mp3' href='http://downloads.bbc.co.uk/learningenglish/features/6min/180719_6min_english_technochauvinism_download.mp3'><span data-i18n-message-id='Download Audio' class='not-translated _bbcle_translate_wrapper' lang='en'>Download Audio</span></a></div>"
final_url = "http://downloads.bbc.co.uk/learningenglish/features/6min/180719_6min_english_technochauvinism_download.mp3"

def _get_file_md5(file_path):
    m = hashlib.md5()

    with open(file_path, "rb") as f:
        while True:
            data = f.read()
            if data:
                m.update(data)
            else:
                break
    return m.hexdigest()


def get_cur_time(time_fmt="%y%m%d"):
    return time.strftime(time_fmt)


def _download_file(url, folder=None, filename=None, filemd5="", log=None, suffix=".mp3", wget_f=False):
    if not folder:
        for di in ["data", get_cur_time()]:
            path = os.path.join(os.getcwd(), di)
            if not os.path.exists(path):
                os.mkdir(path)
            os.chdir(path)
        folder = os.getcwd()
    if not filename:
        filename = get_cur_time() + suffix
    rtn = download_file(url, folder, filename, filemd5, log, wget_f=wget_f)
    if rtn == 0:
        raise Exception("Download file %s failed, try again later." % url)
    return rtn


def download_file(url, folder, filename, filemd5="", d_log=None, checkmd5=False, wget_f=True):
    if not d_log:
        d_log = log

    if not (url and folder and filename):
        d_log.error("no url or folder or filename: %s, %s, %s" %
                    (url, folder, filename))
        return 0

    if not os.path.exists(folder):
        d_log.info("mkdir %s" % folder)
        os.makedirs(folder)

    path = os.path.join(folder, filename)

    if os.path.isfile(path):
        d_log.info("file %s is existing." % path)
        existmd5 = _get_file_md5(path)
        if filemd5 == existmd5:
            d_log.info("same md5")
            return 2

    d_log.info("downloading file from %s" % url)

    success = 0
    for i in range(3):
        if wget_f:
            cmd = "wget -c %s -e robots=off -T 10 -t 10 -P %s" % (url, folder)
            log.info("wget_c: %s" % cmd)
            status = subprocess.call(cmd, shell=True)
            # wget.download(final_url, out=filename)
        else:
            urllib.urlretrieve(url, path)
            d_log.info("download file %s by urlretrieve" % path)
        if filemd5 and checkmd5:
            downloadmd5 = _get_file_md5(path)
            if filemd5 == downloadmd5:
                success = 1
                break
            else:
                d_log.warning("%s error md5 checksum, retry." % url)
        else:
            success = 1
            break

    if not success:
        d_log.warning("download file failed.")
    return success


def if_update(time=None):
    """
    :param time: str like '180809'
    :return:
    """
    if not time:
        time = get_cur_time()
    str_time = str(datetime.now().year)[:2] + time
    date_time = datetime(*time.strptime(str_time, "%Y%m%d")[:3])
    if date_time.weekday() == 4:
        return True

class downBBC(object):
    def __init__(self, time=None, type="mp3"):
        self.type = type
        self.time = time
        self.bs4 = BeautifulSoup(html)
        self.bs4 = BeautifulSoup(urllib.urlopen(base_url).read())


    def get_url(self):
        """
        get the every url about bbc, from the latest,
        :return: dict {time:[url1, url2, ...]}
        """
        if if_update():
            pass


class testBs4(object):
    def __init__(self):
        self.bs4 = BeautifulSoup(html, features="html5lib")

    def test(self):
        return "a"



if __name__ == '__main__':
    zeze = testBs4()
    _download_file(final_url, wget_f=True)
