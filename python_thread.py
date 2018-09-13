# -*- coding:utf-8 -*-
import time
import threading
from threading import Lock # lock.acquire/lock.release
from threading import Semaphore
N = 2
ALL_THREADS = []


def init_thread(name,func,*args,**kwargs):
    t = threading.Thread(name=name,target=func,args=args,kwargs=kwargs)
    ALL_THREADS.append(t)


def start_threads():
    for t in ALL_THREADS:
        t.start()


class Num:
    def __init__(self):
        self.num = 0
        self.sem = Semaphore(value=N)
    def add(self):
        self.sem.acquire()
        self.num += 1
        print(self.num)
        self.sem.release()

if __name__ == '__main__':
    n = Num()
    for _ in range(4):
        n.add()