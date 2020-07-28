#!/usr/bin/env python
# -*- coding:utf-8 -*-

class BaseClass:

    def __init__(self):
        print('init')

    def __call__(self, *args, **kwargs):
        print('call')
        return 1

    def __setitem__(self, key, value):
        print(key, value)

    def __getitem__(self, item):
        print(item, type(item))

    def __delitem__(self, key):
        print(key)


obj = BaseClass()
ret = obj()  # 编写__call__方法后允许调用对象并执行__call__方法
print(ret)
obj['1'] = 1  # 调用__setitem__方法
obj['a']  # 调用__getitem__方法
del obj['2']  # 调用__delitem__方法
obj[1:3]
