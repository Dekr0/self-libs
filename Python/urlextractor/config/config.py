#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
from fake_useragent import UserAgent

APPDATA = os.path.join(os.path.dirname(os.path.dirname(__file__)), "appdata")
REPORT_DIR = os.path.join(APPDATA, r"reports\{}.pdf")
DATABASE = os.path.join(APPDATA, "ReportURLData.mdb")

BASE_URL = r"http://stockdata.stock.hexun.com{}"
INIT_REQUEST = BASE_URL.format(r"/2009_ggqw_{}.shtml")

ADOCONNECTION = r"ADODB.Connection"
ADODBCOMMAND = r"ADODB.Command"
DSN = "PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE={};".format(DATABASE)

PARSER = "lxml"

TITLE_PATTERN = r"\d{{{}}}年({}|{}|{}|{})报告(?!摘要|补充公告|（?正文）?)(?:（?全文）?)?"

USERAGENT = UserAgent().random
