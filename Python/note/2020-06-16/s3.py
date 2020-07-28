#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
提供本地和远程的并发性，如果线程之间不需要任何通信，不建议使用Event
"""
import threading


def task(event):
    print("start...waiting")
    event.wait(60)  # 起到阻塞（blocking）线程的作用，即线程需要等待Event对象（e）内部标识位设为True或超出特定时间（Timeout）时，才能执行
    print("execute...finish")


e = threading.Event()  # 默认标识（flag）位为False
for i in range(10):
    t = threading.Thread(target=task, args=(e,))  # 创建10个线程
    t.start()  # 运行后遇到堵塞
e.clear()  # 确保标识位为False
inp = input("run: y/n? ").strip()
if inp == "y":
    e.set()  # 标识位设置为True
else:
    quit()
