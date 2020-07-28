#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 遇到多重继承关系时


class BaseClass:

    def __init__(self):
        print('BASE INIT')
        self.type = 'base'


class SubClass(BaseClass):

    def __init__(self):
        # super().__init__()
        print('SUB INIT')
        self.x = 'x'


class MyClass(SubClass):

    def __init__(self):
        print('MY INIT')
        self.y = 'y'
        super(MyClass, self).__init__()
        # super(SubClass, self).__init__()
