#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
多线程
"""
import threading
import time


def process(arg):
    time.sleep(1)
    print(arg)


for i in range(10):
    # 创建多个线程，同时处理函数的执行
    t = threading.Thread(target=process, args=(i,))
    t.start()
