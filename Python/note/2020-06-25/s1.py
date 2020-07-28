#!/usr/bin/env python
# -*- coding:utf-8 -*-

# from multiprocessing import process
# import logging
# import sys


def singleton():
    pass


class HandlerGenerator:
    pass


class LoggerGenerator:
    pass


if __name__ == "__main__":
    def decor2(func):
        def index():
            print("index")
            func()

        return index


    def decor1(func):
        def fetch():
            print("fetch")
            func()

        return fetch


    def foo():
        print("foo")


    foo = decor2(decor1(foo))
    foo()