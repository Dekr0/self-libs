#!/usr/bin/env python
# -*- coding:utf-8 -*-

class MyClass:

    var1 = 1
    __var2 = 2

    def __init__(self, pwd):
        self.__pwd = pwd

    def fetch(self):
        print(MyClass.__var2)
        print(self.__pwd)

    def bypass(self):
        self.__index()

    def __index(self):
        print('indexing ' + self.__pwd)

    @staticmethod
    def sign():
        MyClass.__reg()

    @staticmethod
    def __reg():
        print('register')


print(hasattr(MyClass(123), '__index'))
