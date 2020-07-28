#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time


def func(num):
    print(num)


def bypass(num):
    time.sleep(10)
    func(num)


"""
setDaemon为False的时候，主线程将等待3个子线程执行完bypass函数后在结束
为True的时候，主线程不等待3个子线程执行完bypass函数，直接结束
"""
t1 = threading.Thread(target=bypass, args=(1,))
t1.setDaemon(False)
t1.start()
t2 = threading.Thread(target=bypass, args=(2,))
t2.setDaemon(False)
t2.start()
t3 = threading.Thread(target=bypass, args=(3,))
t3.setDaemon(False)
t3.start()
