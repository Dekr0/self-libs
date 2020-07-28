#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from bs4 import BeautifulSoup

"""
<tr>
    <td class="add2">
        <a target="_blank" href="http://stockdata.stock.hexun.com/txt/stock_detail_txt_1207688281.shtml">民生银行：2020年第一季度报告（全文）</a>
    </td>
    <td class="add2_1">
        <a target="_blank" href="http://download.hexun.com/ftp/all_stockdata_2009/all/120\768\1207688281.pdf">查看pdf公告</a>
    </td>
    <td class="add2_1">2020-04-30</td>
</tr>
思路：
1. 首先用正则表达式匹配出需要的字符串
2. 利用匹配到字符串中的parent属性，找出此字符串的父节点（<a>）
3. 找到字符串的父节点后，再次调用这个父节点的parent属性，找出此父节点的父节点（<td>）
4. 找出新父节点后，根据源代码可知，此新父节点的父节点为<tr>，并且有多个兄弟节点
5. 找出这些兄弟节点，即可找到下载链接和日期
"""

import re

def showResult(matchObjs):
    for matchObj in matchObjs:
        print(matchObj)
    print("\n")


_REPORT_TYPE = {
    "第一季度报告": 1,
    "半年度报告": 2,
    "第三季度报告": 3,
    "年度报告": 4
}

# text = "平安银行：2020年第一季度报告全文\n" \
#        "万科A：2020年半年度报告（全文）\n" \
#        "新和成：2019年第三季度报告全文\n" \
#        "白云机场：杂项\n" \
#        "民生银行：2018年半年度报告摘要\n" \
#        "民生银行：2018年半年度报告"

# expr = "：\d{{{}}}年({}|{}|{}|{})(（?全文）?)?".format(4, *_REPORT_TYPE.keys())
# pattern = re.compile(exp)  # "：\d{4}年(第一季度|半年度|第三季度|年度)报告(（?全文）?)?"

with open("src.html") as f:
    # soup = BeautifulSoup(f.read(), "lxml")
    # report_title = soup.find(string=re.compile(expr))
    # print(report_title)
    # string_td = report_title.parent.parent
    # url_td = string_td.next_sibling
    # date_td = url_td.next_sibling
    # url = url_td.contents[0].attrs["href"]
    # date = date_td.string
    soup = BeautifulSoup(f.read(), "lxml")
    tag_a = soup.find(name="a", attrs={"href": re.compile(r"^/200\d/ggqw.aspx\?(page=\d{2,3}&stockid=\d{6})"
                                                          "|(stockid=\d{6}&page=\d{2,3})")})  # Need to be optimized

    raw_url = tag_a.attrs["href"]
    pattern = re.compile(r"page=(?P<page_number>\d{2,3})")
    last_page = pattern.search(raw_url).group("page_number")
    raw_url = pattern.sub("page={}", raw_url)
