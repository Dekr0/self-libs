#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

server = socket.socket()  # 创建socket对象以便调用socket内部工具
server.bind(('127.0.0.1', 9000))  # 绑定IP和Port
server.listen(5)  # 设置监听（待处理）连接的个数
while True:
    conn, addr = server.accept()  # 阻塞（即等待，直到incoming连接才继续执行）；建立连接
    conn.sendall(bytes('connected', encoding='utf-8'))
    print(conn, addr)
    while True:
        data = str(conn.recv(1024), encoding='utf-8')
        if data.lower() == 'quit':
            break
        conn.sendall(bytes(data.center(5), encoding='utf-8'))
