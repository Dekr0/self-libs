#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
E:\Src\Python\FTP\ClientSite\bin
python ClientSiteLauncher.py start -i 127.0.0.1 -p 9000
python ClientSiteLauncher.py register -i 127.0.0.1 -p 9000
'''

import sys
sys.path.insert(0, 'E:/Src/Python/FTP/ClientSite/libs')
import client

if __name__ == '__main__':
    client.Client(sys.argv)