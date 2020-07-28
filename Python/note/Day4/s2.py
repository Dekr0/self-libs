#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
while True:
    msg = input('>>>')
    sk.sendall(bytes(msg, encoding='utf-8'))
    if msg == 'quit':
        break
    else:
        data = str(sk.recv(1024), encoding='utf-8')
        print(data)
sk.close()
