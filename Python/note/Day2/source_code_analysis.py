#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello World")


application = tornado.web.Application([(r"/", MainHandler), ])  # 解读 - 1

if __name__ == "__main__":
    application.listen(8888)  # 解读 - 2
    tornado.ioloop.IOLoop.instance().start()  # 解读 - 3
