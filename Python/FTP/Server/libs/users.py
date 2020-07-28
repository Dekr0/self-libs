#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config'))
import config

class Users:

    def __init__(self, usr):
        self.usr = usr
        self.usr_file_path = os.path.join(config.USERSDATA_DIR, usr)
        self.cwd = ['~']
        self.cwd_actual = [self.usr_file_path]
