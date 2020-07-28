#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import json

IP_PORT = ('127.0.0.1', 9000)

sender = socket.socket()
sender.connect_ex(IP_PORT)
dic = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
data = json.dumps(dic)
sender.sendall(bytes(data, encoding='utf-8'))
sender.close()
