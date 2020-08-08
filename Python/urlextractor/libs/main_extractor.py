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

_INIT_REQUEST - Initial URL of report release page. Can be used as a formatted string to visit page of a specific stock.
This initial URL always points to a first page of the report release webpage of a specific stock

_PARSER - Name of the html parser being used in BS4

_SIZE - Buffer size - for future used

_SRC - Path to reports folder - for future used

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
            sys.exit("Failed to connect ot database: {}".format(ex))

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
    reportURL_list = []

    while not rs.EOF:
        url = rs.Fields("网址").Value
        reportURL_list.append(url)
        rs.MoveNext()

    return rs, reportURL_list


_CONN = __get_conn()
_INSERT, _PARAMS = __get_command(_CONN)
_REPORT_TYPE = __get_report_type(_CONN)
_STOCK_IDS = __get_stock_id(_CONN)
_LATEST_YEAR = __get_latest_year(_CONN)
(_URLTABLE, _REPORTURL_LIST) = __get_url_table(_CONN)
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
        logging.info("Process finish")

        self.__refactor()
        logging.info("Refactored and cleaned up\n")

    @staticmethod
    def __get_page(src):
        """
        Get the "page" parameter from the URL of webpage where all reports of a specific stock are released. From the
        source code, this URL is different from the URL (refereed as initial URL) that is used to request source from
        the webpage. The initial URL does not contain the part that is "page=...&stockid=...".

        "page" and "stockid" act as parameters which allow you to navigate specific page of the report release webpage
        by specific stock. The only parameter needed is page since all the stock ID is already known.
        :return:
        """

        # Search tag <a> with specific attributes (href). \d{2,3} helps to ignore one of tag <a> with attribute href
        # whose URL has single digit (means first page) in page parameter

        soup = BeautifulSoup(src, "lxml")
        tag_a = soup.find(name="a", attrs={"href": re.compile(r"^/200\d/ggqw.aspx\?(?:page=\d{2,3}&stockid=\d{6})"
                                                              "|(?:stockid=\d{6}&page=\d{2,3})")})

        raw_url = tag_a.attrs["href"]
        pattern = re.compile(r"page=(?P<last_page>\d{2,3})")
        last_page = pattern.search(raw_url).group("last_page")

        pageurl = pattern.sub("page={}", raw_url)  # Replace the "page" parameter with "{}" so it can be formatted

        # Attach the formatted URL to URL of the main page of stockdata.stock.hexun.com
        url = _BASE_URL.format(pageurl)

        return url, int(last_page)

    @staticmethod
    def __request(referrer):
        """
        Sending request to the website and return its source code
        :return:
        """

        header = {
            "user-agent": _USERAGENT,
            "referrer": referrer
        }
        try:
            response = requests.get(referrer, headers=header)
            src = response.text
            response.close()
        except Exception as ex:
            logging.critical("Line 282: {}".format(ex))

        return src

    @staticmethod
    def __refactor():
        """
        Refactor
        Close all the RecordSet objects; disconnect with the database; empty all the list and the dictionary consisted
        of large amount information.
        :return:
        """

        global _CONNS, _USERAGENT, _CONN, _INSERT, _PARAMS, _REPORT_TYPE, _STOCK_IDS, _URLTABLE, _REPORTURL_LIST
        _URLTABLE.Close()
        _CONN.Close()

        _CONNS.clear()
        _REPORTURL_LIST.clear()

        _USERAGENT = None
        _INSERT = None
        _PARAMS = None
        _REPORT_TYPE = None
        _STOCK_IDS = None

    @staticmethod
    def __update(report_info):
        """
        Insert report information into database
        :return:
        """

        for i in _PARAMS.keys():
            _PARAMS[i].Value = report_info[i]
        _INSERT.Execute()

    def __analy_rurl(self):
        """
        Analyze the raw report information from the source code. Filter, sort and store each of them into a dictionary.
        A list will hold all the dictionary.
        :return:
        """

        for url_dict in self.rurl_list:
            title = list(url_dict.keys())[0]

            pattern = "(?P<type>{}|{}|{}|{})".format(*_REPORT_TYPE.keys())
            report_type = _REPORT_TYPE[re.search(pattern, title).group("type")]  # Get which type of report is it

            # The key of the dictionary is correspond to the name of the unfilled, customized parameter attached to the
            # Command object that is used for insertion.
            report_info = {
                "stock_id": self.stock_id,
                "stock_name": _STOCK_IDS[self.stock_id],
                "year": url_dict[title]["Year"],
                "report_type": report_type,
                "url": url_dict[title]["URL"]
            }
            self.report_list.append(report_info)

        self.rurl_list.clear()
        logging.info("released memory space from rurl_list")

    def __cycle_page(self, url, last_page):
        """
        Flip page in the report release webpage. Get the title, URL, and the release date of the report.
        The stop factor of this process depends on the latest year of all report in the database.

        **Note** - might rewrite this method with recursion

        :param url:
        :param last_page:
        :return:
        """

        logging.info("start cycling page")
        page = 1

        while page < last_page:
            src = self.__request(url.format(page))
            flag = self.__get_url(src)
            page += 1

            if not flag:
                # Either no matched report in this page or matched report already in the database
                continue

            elif flag == -1:
                # If the current page only contains report whose year is older than the latest year, then stop
                # this process.
                break

            time.sleep(1)

        logging.info("{} pages are cycled".format(page))

    def __get_url(self, src):
        """
        Get the title, URL, and the release date of the report, and return the stop fator of the page flipping process.
        :return:
        """

        soup = BeautifulSoup(src, "lxml")
        titles = soup.find_all(string=re.compile(_TITLE_PATTERN))
        flag = 0
        if not titles:
            return flag
        for title in titles:
            title_td = title.parent.parent
            url_td = title_td.next_sibling
            date_td = url_td.next_sibling
            url = url_td.contents[0].attrs["href"]
            redate = str(date_td.string)  # 发表日期
            year = int(re.compile(r"(?P<year>\d{4})").search(str(title)).group("year"))  # 报告年份
            if year >= _LATEST_YEAR:
                if url not in _REPORTURL_LIST:
                    flag += 1
                    self.rurl_list.append({str(title): {"ReleasedDate": redate, "Year": year, "URL": url}})
        if not flag:
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

            # Request source code from the webpage where all the report of a specific are released by using the initial
            # URL
            src = self.__request(_INIT_REQUEST.format(self.stock_id))

            (url, last_page) = self.__get_page(src)

            self.__cycle_page(url, last_page)

            if self.rurl_list:
                self.__analy_rurl()
                logging.info("prepare to write {}".format(stock_id))

                for report_info in self.report_list:
                    self.__update(report_info)

                logging.info("{} new reports are updated".format(len(self.report_list)))
                self.report_list.clear()
                logging.info("released memory space from report_list")


            logging.info("{} finished".format(stock_id))
