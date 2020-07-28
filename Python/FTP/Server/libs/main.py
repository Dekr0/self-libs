#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import server
import socketserver
import json
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config'))
import config


class Main:

    def __init__(self, args):
        self.r_args = args
        self.rscdict = {
            40: 'Arguments required',
            41: 'Not enough arguments',
            42: 'Invalid formatting',
            43: 'This is not a built-in command',
            44: 'Invalid port',
        }
        self.__args_parse()

    def __args_parse(self):
        if self.r_args:
            try:
                p_args = self.r_args[1:6]
            except IndexError:
                self.__statushandler(41)
            else:
                if '-i' in p_args and '-p' in p_args:
                    if hasattr(self, p_args[0]):
                        func = getattr(self, p_args[0])
                        try:
                            self.ip = p_args[p_args.index('-i') + 1]
                            self.port = int(p_args[p_args.index('-p') + 1])
                        except ValueError:
                            self.__statushandler(44)
                        else:
                            func()
                    else:
                        self.__statushandler(43)
                else:
                    self.__statushandler(42)
        else:
            self.__statushandler(40)

    def __statushandler(self, rsn):
        print(self.rscdict[rsn])

    def start(self):
        try:
            print("starting...")
            _server = socketserver.ThreadingTCPServer((self.ip, self.port), server.Server)
            print("server started")
            server.Server.load_usr_accounts()
            print("Users's account loaded")
            _server.serve_forever()
        except KeyboardInterrupt:
            # 处理出现Ctrl-C后报错的方法
            pass
