#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import sys

client = socket.socket()
print('waiting')
client.connect(('127.0.0.1', 9000))
intro = str(client.recv(1024), encoding='utf-8')  # 阻塞（即等待，直到数据传入才继续执行）；接收数据
print(intro)
while True:
    msg = input('>>>')
    client.sendall(bytes(msg, encoding='utf-8'))
    if msg.lower() == 'quit':
        sys.exit()
