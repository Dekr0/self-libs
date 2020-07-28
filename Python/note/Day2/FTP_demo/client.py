#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import os

IP_PORT = ('127.0.0.1', 9000)
size = str(os.stat('file.CT').st_size)
print(size)
client = socket.socket()
client.connect(IP_PORT)
client.sendall(bytes(size, encoding='utf-8'))
guard = int(str(client.recv(1024), encoding='utf-8'))
if guard == 1:
    with open('file.CT', 'rb') as file:
        for line in file:
            client.sendall(line)
client.close()
