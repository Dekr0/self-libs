#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
while True:
    msg = input('>>>')
    if msg.lower() == 'quit':
        break
    client.sendto(bytes(msg, encoding='utf-8'), ('127.0.0.1', 9000))
    data = str(client.recv(1024), encoding='utf-8')
    print(data)
client.close()
