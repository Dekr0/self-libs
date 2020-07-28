#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

IP_PORT = ('127.0.0.1', 9000)
server = socket.socket()
server.bind(IP_PORT)
server.listen(5)
conn, addr = server.accept()
size = int(str(conn.recv(1024), encoding='utf-8'))
conn.sendall(bytes('1', encoding='utf-8'))
process = 0
file = open('new_file.CT', 'wb')
while process != size:
    data = conn.recv(1024)
    file.write(data)
    process += len(data)
file.close()
server.close()
