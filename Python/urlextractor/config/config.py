#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
from fake_useragent import UserAgent

APPDATA = os.path.join(os.path.dirname(os.path.dirname(__file__)), "appdata")
ADOCONNECTION = r"ADODB.Connection"
ADODBCOMMAND = r"ADODB.Command"
BASE_URL = "http://stockdata.stock.hexun.com{}"
DATABASE = os.path.join(APPDATA, "ReportURLData.mdb")
DSN = "PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE={};".format(DATABASE)
INIT_REQUEST = BASE_URL.format("/2009_ggqw_{}.shtml")
PARSER = "lxml"
SRC = os.path.join(APPDATA, "temp\\{}.txt")
TITLE_PATTERN = r"\d{{{}}}年({}|{}|{}|{})报告(?!摘要|补充公告|（?正文）?)(?:（?全文）?)?"
USERAGENT = UserAgent().random


