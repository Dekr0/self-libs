#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This is a script (mostly for own use, actually helping one of my friends lol) that will fetch all the download link
the report of stock from website http://stockdata.stock.hexun.com based on different needs (specific title format,
specific report type, etc.). The script is still under developed.

Constant Variables:

_ADOCONNECTION, _ADODBCOMMAND - Constant strings that store the name of ADO object

_BASE_URL - URL of the website's main page. Can be used as a formatted string for visit specific section the website

_CONNS - List of connections for database. It always only has one ADO Connection object

_DATABASE - File path of the database

_DSN - A connection string (include several parameters. i.e. ODBC driver)

_INIT_REQUEST - Initial URL of report release page. Can be used as a formatted string to visit page of a specific stock

_PARSER - Name of the html parser being used in BS4

_SIZE - Buffer size - for future used

_SRC - Path to temp folder - for future used

_USERAGENT - A faked, randomized useragent for request header

_TITLE_PATTERN - Prepare an regex expression for searching specific report's title. Can be formatted based on specific
need. (After formatted: \d{4}年(第一季度|半年度|第三季度|年度)报告(?!摘要|补充公告|（?正文）?)(?:（?全文）?)? )
"""

import logging
import os
import sys
import re
import requests
import time
from bs4 import BeautifulSoup
from win32com import client

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__name__)), "config"))
from config import config
from config.ADOConstants import *


_ADOCONNECTION = config.ADOCONNECTION
_ADODBCOMMAND = config.ADODBCOMMAND
_BASE_URL = config.BASE_URL
_CONNS = []
_DATABASE = config.DATABASE
_DSN = config.DSN
_INIT_REQUEST = config.INIT_REQUEST
_PARSER = config.PARSER
_SIZE = 1024
_SRC = config.SRC
_USERAGENT = config.USERAGENT


def __get_command(conn):
    """
    Create an modified ADO Command object with unfilled, customized parameters for insert data into the database.
    :param conn: ADO Connection object instance
    :return:
    """
    cmd = client.Dispatch(_ADODBCOMMAND)  # Create an ADO Command object instance
    cmd.ActiveConnection = conn  # Attach to an ADO Connection object instance
    cmd.CommandType = adCmdText  # Type of command being used

    # VALUES (?, ?, ?, ?, ?) will reserve 5 empty slots for 5 unfilled, customized parameters, "?" act as a placeholder
    query = "INSERT INTO PDF网址(股票代码, 股票名称, 年度, 报告编号, 网址) VALUES (?, ?, ?, ?, ?)"
    cmd.CommandText = query

    # A dictionary that stores the ADO Parameter object instance
    params = dict()

    # Create Parameter object instances and setup their properties
    params["stock_id"] = cmd.CreateParameter("stock_id", adVarChar, adParamInput, _SIZE)
    params["stock_name"] = cmd.CreateParameter("stock_name", adVarChar, adParamInput, _SIZE)
    params["year"] = cmd.CreateParameter("year", adInteger, adParamInput)
    params["report_type"] = cmd.CreateParameter("report_type", adInteger, adParamInput)
    params["url"] = cmd.CreateParameter("url", adVarChar, adParamInput, _SIZE * 4)
    params["year"].NumericScale = 0
    params["report_type"].NumericScale = 0

    # Attach Parameter object instances just created to an Command object instance
    for i in params.keys():
        cmd.Parameters.Append(params[i])
    cmd.Prepared = True  # Ready to be used
    return cmd, params


def __get_conn():
    """
    Initialize a connection object which hold the connection with the database. Only one connection object is allowed
    :return:
    """
    if not _CONNS:
        try:
            conn = client.Dispatch(_ADOCONNECTION)
            conn.Open(_DSN)
            if conn.State == adStateOpen:  # Check whether the connection is open
                _CONNS.append(conn)
                return _CONNS[0]
            raise Exception
        except Exception as ex:
            print("Failed to connect ot database: {}".format(ex))
    return _CONNS[0]


def __get_latest_year(conn):
    """
    Get the latest year in all the report's year. To prevent the script fetching the url of old reports / reports that
    already exist, which consumes unnecessary time.
    :param conn:
    :return:
    """
    query = "SELECT MAX(年度) AS latest_year FROM PDF网址"
    (rs, result) = conn.Execute(query)
    latest_year = int(rs.Fields("latest_year").Value)
    return latest_year


def __get_stock_id(conn):
    """
    Get the id and name of all stocks and store them in a dictionary. Keys will be the id of the stock; Value will be
    the name of the stock
    :param conn:
    :return:
    """
    sc = dict()
    query = "SELECT 股票代码, 股票名称 FROM 股票代码"
    (rs, result) = conn.Execute(query)
    while not rs.EOF:
        sc[rs.Fields("股票代码").Value] = rs.Fields("股票名称").Value
        rs.MoveNext()
    rs.Close()
    return sc


def __get_report_type(conn):
    """
    Get the name of each report type and its corresponded id, and store them in a dictionary. Keys will be the name of
    the report type; Value will be the id of the report type.
    :param conn:
    :return:
    """
    rt = dict()
    query = "SELECT * FROM 报告类型"
    (rs, result) = conn.Execute(query)
    while not rs.EOF:
        rt[rs.Fields("报告类型").Value] = int(rs.Fields("报告编码").Value)
        rs.MoveNext()
    rs.Close()
    return rt


def __get_url_table(conn):
    """
    Initialize a RecordSet object of the table named "PDF网址"
    Get all the existed report information from this table, and store them in the list (report_list). A report and its
    information will be stored in a dictionary. A dictionary that contains information of a report will be a element of
    the list. The list will be used to prevent inserting the exact same report information into the database.

    **Note**: anyway to optimize? without drawing all existed information in the list, and handling this issue within
    the database by using ADO method / object and SQL language

    :param conn:
    :return:
    """
    query = "SELECT * FROM PDF网址"
    (rs, result) = conn.Execute(query)
    report_list = []
    while not rs.EOF:
        stock_id = rs.Fields("股票代码").Value
        stock_name = rs.Fields("股票名称").Value
        season = rs.Fields("年度").Value
        report_type = rs.Fields("报告编号").Value
        url = rs.Fields("网址").Value
        report_list.append({"stock_id": stock_id,
                            "stock_name": stock_name,
                            "season": int(season),
                            "report_type": int(report_type),
                            "url": url})
        rs.MoveNext()
    return rs, report_list


_CONN = __get_conn()
_INSERT, _PARAMS = __get_command(_CONN)
_REPORT_TYPE = __get_report_type(_CONN)
_STOCK_IDS = __get_stock_id(_CONN)
_LATEST_YEAR = __get_latest_year(_CONN)
(_URLTABLE, _REPORT_LIST) = __get_url_table(_CONN)
_TITLE_PATTERN = config.TITLE_PATTERN.format(4, *_REPORT_TYPE.keys())

def singleton(cls, *args, **kwargs):
    _instance = []

    def _singleton():
        if not _instance:
            _instance.append(cls(*args, **kwargs))
        return _instance[0]

    return _singleton


@singleton
class URLExtractor:

    def __init__(self):
        # Create a list that temporarily stores the unprocessed report information of a stock, each element will be a
        # dictionary that stored a unprocessed information of a report
        self.rurl_list = []

        # Create a list that temporarily stores the processed report information of a stock, each element will be a
        # dictionary. Prepare for insertion
        self.report_list = []
        self.__handle()

    @staticmethod
    def __get_page(src):
        """
        Get the "page" parameter from the URL of webpage where all reports of a specific stock are released. From the
        source code, this URL is different from the URL (refereed as initial URL) that is used to request source from
        the webpage. The initial URL
        :return:
        """
        # with open(_SRC.format(code)) as f:
        soup = BeautifulSoup(src, "lxml")
        tag_a = soup.find(name="a", attrs={"href": re.compile(r"^/200\d/ggqw.aspx\?(?:page=\d{2,3}&stockid=\d{6})"
                                                              "|(?:stockid=\d{6}&page=\d{2,3})")})
        # Need to be optimized

        raw_url = tag_a.attrs["href"]
        pattern = re.compile(r"page=(?P<last_page>\d{2,3})")
        last_page = pattern.search(raw_url).group("last_page")  # might have problem
        pageurl = pattern.sub("page={}", raw_url)  # i.e: /2008/ggqw.aspx?page={}&stockid=code
        url = _BASE_URL.format(pageurl)  # i.e: http://stockdata.stock.hexun.com/2008/ggqw.aspx?page={}&stockid=code

        return url, int(last_page)

    @staticmethod
    def __request(referrer):
        """
        向网站发送请求
        :return:
        """
        header = {
            "user-agent": _USERAGENT,
            "referrer": referrer
        }

        response = requests.get(referrer, headers=header)
        src = response.text
        response.close()

        # with open(_SRC.format(code), "wb") as f:
        #     f.write(response.content)

        return src

    @staticmethod
    def __update(report_info):
        """
        将URL写入Access中
        :return:
        """
        for i in _PARAMS.keys():
            _PARAMS[i].Value = report_info[i]
        _INSERT.Execute()

    def __analy_rurl(self):
        """
        整理/处理URL，股票名称，股票代码，报告类型，整备写入
        :return:
        """
        for url_dict in self.rurl_list:
            title = list(url_dict.keys())[0]
            pattern = "(?P<type>{}|{}|{}|{})".format(*_REPORT_TYPE.keys())
            report_type = _REPORT_TYPE[re.search(pattern, title).group("type")]
            report_info = {
                "stock_id": self.stock_id,
                "stock_name": _STOCK_IDS[self.stock_id],
                "year": url_dict[title]["Year"],
                "report_type": report_type,
                "url": url_dict[title]["URL"]
            }
            if report_info not in _REPORT_LIST:
                self.report_list.append(report_info)
        self.rurl_list.clear()  # 释放内存空间
        logging.info("released memory space from rurl_list")

    def __cycle_page(self, url, last_page):
        logging.info("start cycling page")
        page = 1
        while page < last_page:
            src = self.__request(url.format(page))
            flag = self.__get_url(src)  # 未处理的URL和发表日期
            page += 1
            if not flag:
                # 此页没有匹配对象
                continue
            elif flag == -1:
                # 此页由于年份过久而没有匹配对象，并不再往下进行搜索
                break
            time.sleep(1)
        logging.info("{} pages are cycled".format(page))

    def __get_url(self, src):
        """
        抓取下载URL
        :return:
        """
        soup = BeautifulSoup(src, "lxml")
        titles = soup.find_all(string=re.compile(_TITLE_PATTERN))
        """
        r"\d{4}年({第一季度}|{半年度}|{第三季度}|{年度})报告(?!摘要|补充公告|（?正文）?)(?:（?全文）?)?"
        """
        flag = 0
        if not titles:
            # 此页没有匹配对象
            return flag
        for title in titles:
            title_td = title.parent.parent
            url_td = title_td.next_sibling
            date_td = url_td.next_sibling
            url = url_td.contents[0].attrs["href"]
            redate = str(date_td.string)  # 发表日期
            year = int(re.compile(r"(?P<year>\d{4})").search(str(title)).group("year"))  # 报告年份
            if year >= 2010:
                # 在2010年之后报告不收入字典类
                flag += 1
                self.rurl_list.append({str(title):
                                           {"ReleasedDate": redate,
                                            "Year": year,
                                            "URL": url}
                                       })
        if not flag:
            # 此页由于年份过久而没有匹配对象
            flag -= 1
        return flag

    def __handle(self):
        """
        Essential logical structure of the script
        :return:
        """
        for stock_id in _STOCK_IDS.keys():
            logging.info("handling {}".format(stock_id))
            self.stock_id = stock_id

            # Request source code from the webpage where all the report of a specific are released.
            src = self.__request(_INIT_REQUEST.format(self.stock_id))
            (url, last_page) = self.__get_page(src)
            self.__cycle_page(url, last_page)

            self.__analy_rurl()
            logging.info("prepare to write {}".format(stock_id))

            for report_info in self.report_list:
                self.__update(report_info)
            self.report_list.clear()

            logging.info("released memory space")
            logging.info("{} finished".format(stock_id))
        _URLTABLE.Close()
        _CONN.Close()
