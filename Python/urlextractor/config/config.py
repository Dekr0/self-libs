#!/usr/bin/env python
# -*- coding:utf-8 -*-


from os import path
from fake_useragent import UserAgent
import re

APPDATA = path.abspath(path.join(path.dirname(path.dirname(__file__)), r"appdata"))
DATABASE = path.abspath(path.join(APPDATA, r"database\report_url.mdb"))
REPORT_DIR = path.abspath(path.join(APPDATA, r"report\{}.pdf"))
PHRASE_LIB = path.abspath(path.join(APPDATA, r"word_phrase.json"))

BASE_URL = r"http://stockdata.stock.hexun.com{}"
INIT_REQUEST = BASE_URL.format(r"/2009_ggqw_{}.shtml")

ADOCONNECTION = r"ADODB.Connection"
ADODBCOMMAND = r"ADODB.Command"
DSN = r"PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE={};".format(DATABASE)

CN_NUM = {"零": "0", "〇": "0", "一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8",
          "九": "9", "0": "0", 0: "0"}
TITLE_PATTERN = r"：([零〇一二三四五六七八九]|\d){{{}}}年({}|{}|{}|{})报告(?:（?全文）?|（?更新后）?)?$"

USERAGENT = UserAgent().random
