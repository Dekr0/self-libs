#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
E:\Src\Python\FTP\Server\bin
python ServerLauncher.py start -i 127.0.0.1 -p 9000
'''

import sys
sys.path.insert(0, 'E:/Src/Python/FTP/Server/libs')
import main

if __name__ == '__main__':
    main.Main(sys.argv)