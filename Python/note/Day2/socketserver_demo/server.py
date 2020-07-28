#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socketserver

IP_PORT = ('127.0.0.1', 9000)


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('running')
        conn = self.request
        addr = self.client_address
        conn.sendall(bytes('connected', encoding='utf-8'))
        print(conn, addr)
        while True:
            data = str(conn.recv(1024), encoding='utf-8')


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(IP_PORT, MyServer)
    server.serve_forever()
