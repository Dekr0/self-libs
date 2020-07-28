#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

BUFFER_SIZE = 1024
ROOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))
CONFIG_DIR = os.path.join(ROOT_DIR, 'config')
USERSDATA_DIR = os.path.join(ROOT_DIR, 'usersdata')
USER_ACCOUNTS_FILE = os.path.join(CONFIG_DIR, 'userskey.psw')
