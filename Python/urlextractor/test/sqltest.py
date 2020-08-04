#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from win32com import client


conn = client.Dispatch(r"ADODB.Connection")
conn.Open(r"PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=D:\Dekr0\self-libs\Python\urlextractor\appdata\ReportURLData.mdb")
query = r"SELECT * FROM PDF网址 WHERE 股票代码='000001' AND 年度=2012 AND 报告编号=5"
count = r"SELECT COUNT(*) AS NumOfResult FROM ({})".format(query)
(com, result) = conn.Execute(count)
print(type(com.Fields("NumOfResult").Value))
# if int(com.GetString()) >= 1 :
#     (rs, result) = conn.Execute(query)
#     while not rs.EOF:
#         print(rs.Fields("网址").Value)
#         rs.MoveNext()
#     rs.Close()