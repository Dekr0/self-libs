#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
读写分离
"""
import socket
import select

IP_PORT = ('127.0.0.1', 9000)

server = socket.socket()
server.bind(IP_PORT)
server.listen()

in_list = [server, ]  # 输入
out_list = []  # 输出
error_list = []  # 出错

data_dict = {}  # 字典：储存已连接请求发送的数据

while True:
    # 尝试模拟queue模块的运作方式（使用字典和列表伪造这种效果）
    rlist, wlist, xlist = select.select(in_list, out_list, error_list, 1)
    print('Number of objects being listened: {}'.format(len(in_list)))
    for i in rlist:
        if i == server:
            conn, addr = server.accept()
            in_list.append(conn)
            data_dict[conn] = []  # 为特定的请求创建一个自己的数据列表
        else:
            try:
                data = str(i.recv(1024), encoding='utf-8')
            except Exception as e:
                in_list.remove(i)
            else:
                if data == 'quit':
                    in_list.remove(i)
                else:
                    data_dict[i].append(data)
                    out_list.append(i)  # 将发送数据的请求放入输出列表
    for i in wlist:
        # 可用队列进行优化
        data = data_dict[i][0].center(5)
        del data_dict[i][0]
        i.sendall(bytes(data, encoding='utf-8'))
        out_list.remove(i)
    for i in xlist:
        in_list.remove(i)
