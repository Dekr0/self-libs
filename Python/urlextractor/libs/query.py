#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__name__)), "config"))
from .ado_util import ADOUtil
from .gui import show


class ReportQuery(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(ReportQuery, "_instance"):
            ReportQuery._instance = object.__new__(cls)
        return ReportQuery._instance

    def __init__(self):
        self.__util = ADOUtil()
        self.__handle()

    def __handle(self):
        show(self.__util.conn, self.__util.get_report_type())
