#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import json

IP_PORT = ('127.0.0.1', 9000)

sender = socket.socket()
sender.bind(IP_PORT)
sender.listen(5)
conn, addr = sender.accept()
data = json.loads(str(conn.recv(2048), encoding='utf-8'))
print(data, type(data))
sender.close()
