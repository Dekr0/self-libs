#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import select
# select - windows专用，poll是对select的优化, epoll使用异步（通过文件描述符的反馈进行监听，非循环）
# 模块概念类似，但是底层调用机制不相同

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 9000))
sk1.listen(5)

sk2 = socket.socket()
sk2.bind(('127.0.0.1', 9001))
sk1.listen()

sk3 = socket.socket()
sk3.bind(('127.0.0.1', 9002))
sk1.listen()

# sklist = [sk1, sk2, sk3,]
sklist = [sk1, ]

while True:
    # 伪并发
    # 伪造同时处理多个请求，本质是在连接所有请求后逐个处理
    rlist, wlist, xlist = select.select(sklist, [], sklist, 1)  # 1表示每次监听之间的时间间隔
    # xlist的一个用处就是移除出错的套接字，避免程序出错
    # wlist，监听等待直到准备写入，只要参数列表有值，返回参数列表
    print('Number of sockets being listened: {}'.format(len(sklist)))
    for i in rlist:
        # 每一个连接对象
        if i == sk1:
            # sk1只接受客户的连接
            conn, addr = i.accept()
            conn.sendall(bytes('connected', encoding='utf-8'))
            sklist.append(conn)
        else:
            # 已连接请求的交互
            try:
                data = str(i.recv(1024), encoding='utf-8')
            except Exception as ex:
                # 请求的连接出现异常，移除（例如请求强行终止）
                sklist.remove(i)
            else:
                if data == 'quit':
                    sklist.remove(i)
                else:
                    i.sendall(bytes(data.center(5), encoding='utf-8'))
    for i in xlist:
        sklist.remove(i)
