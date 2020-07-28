#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        pass


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000,), MyServer)
    print(type(server))
    server.serve_forever()
