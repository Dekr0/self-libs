#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
server.bind(('127.0.0.1', 9000))
while True:
    bdata, addr = server.recvfrom(1024)
    sdata = str(bdata, encoding='utf-8')
    if sdata.lower() == 'quit':
        break
    server.sendto(bytes(sdata.center(5), encoding='utf-8'), addr)
