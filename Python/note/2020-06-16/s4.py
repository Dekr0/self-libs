#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time


def task(num):
    print(num)


def bypass(num):
    time.sleep(10)
    task(num)


num = 1
thread1 = threading.Thread(target=bypass, args=(num,))
thread1.start()
thread1.join()  # 主线程被阻塞，等待thread1执行完毕 - 结果：等约10秒
num += 1
print(num)
thread2 = threading.Thread(target=bypass, args=(num,))
thread2.start()
thread2.join(1)  # 主线程被阻塞，等待thread2执行完毕，最多等1秒，否则继续往下执行 - 等约1秒
num += 1
print(num)
thread3 = threading.Thread(target=bypass, args=(num,))
thread3.start()
