#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time

lock = threading.RLock()
num = 0


def count():
    lock.acquire()  # 获得一把锁
    global num
    num += 1
    time.sleep(1)
    print(num)
    lock.release()  # 释放锁


t = threading.Thread(target=count)
t.start()

for i in range(10):
    print("main {}".format(i))
