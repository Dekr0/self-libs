"""

This is a script (mostly for own use) that will fetch all the download link the report of stock from website
http://stockdata.stock.hexun.com based on different needs (specific title format, specific report type, etc.).

The script is still under developed.

"""

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import os
import sys
import re
import requests
import time
from bs4 import BeautifulSoup

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__name__)), "config"))
from .ado_util import *
from config.config import *


_BASE_URL = BASE_URL
_INIT_REQUEST = INIT_REQUEST
_USERAGENT = USERAGENT


def get_page(src):
    """
    Get the "page" parameter from the URL of webpage where all report of a specific stock are released. From the
    source code, this URL is different from the URL (refereed as initial URL) that is used to request source from
    the webpage. The initial URL does not contain the part that is "page=...&stockid=...".

    "page" and "stockid" act as parameters which allow you to navigate specific page of the report release webpage
    by specific stock. The only parameter needed is page since all the stock ID is already known.
    """

    # Search tag <a> with specific attributes (href). \d{2,3} helps to ignore one of tag <a> with attribute href
    # whose URL has single digit (means first page) in page parameter

    soup = BeautifulSoup(src, "lxml")
    tag_a = soup.find(name="a", attrs={"href": re.compile(r"^/200\d/ggqw.aspx\?(?:page=\d{2,3}&stockid=\d{6})"
                                                          "|(?:stockid=\d{6}&page=\d{2,3})")})

    raw_url = tag_a.attrs["href"]
    pattern = re.compile(r"page=(?P<last_page>\d{2,3})")
    last_page = pattern.search(raw_url).group("last_page")

    pageurl = pattern.sub("page={}", raw_url)
    url = _BASE_URL.format(pageurl)

    return url, int(last_page)


def request(referrer):
    header = {
        "user-agent": _USERAGENT,
        "referrer": referrer
    }
    src = str()
    try:
        response = requests.get(referrer, headers=header)
        src = response.text
        response.close()
    except Exception as ex:
        logging.critical(ex)

    return src


class URLCrawler(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(URLCrawler, "_instance"):
            URLCrawler._instance = object.__new__(cls)
        return URLCrawler._instance

    def __init__(self):
        self.__util = ADOUtil()
        self.__conn = self.__util.conn
        self.__insert, self.__params = self.__util.get_command()
        self.__latest_year = self.__util.get_latest_year()
        self.__report_type = self.__util.get_report_type()
        self.__stock_list = self.__util.get_stock_id()
        self.__url_list = self.__util.get_url_list()
        self.__title_pattern = TITLE_PATTERN.format(4, *self.__report_type.keys())

        self.rurl_list = []  # URLs and their un-processed information
        self.report_list = []  # URLs and their processed information

        self.__handle()
        logging.info("Process finish")

        self.__refactor()
        logging.info("Refactored and cleaned up\n")

    def __refactor(self):
        self.__conn.Close()
        self.__report_type.clear()
        self.__stock_list.clear()
        self.__url_list.clear()
        self.__insert = None
        self.__params = None
        self.__util = None

    def __update(self, report_info):
        for i in self.__params.keys():
            self.__params.Value = report_info[i]
        self.__insert.Execute()

    def __analy_rurl(self):
        """
        Analyze the raw report information from the source code. Filter, sort and store each of them into a dictionary.
        A list will hold all the dictionary.
        """
        
        for url_dict in self.rurl_list:
            title = list(url_dict.keys())[0]

            pattern = "(?P<type>{}|{}|{}|{})".format(*self.__report_type.keys())
            report_type = self.__report_type[re.search(pattern, title).group("type")]

            # The key of the dictionary is correspond to the name of the unfilled, customized parameter attached to the
            # Command object that is used for insertion.
            report_info = {
                "stock_id": self.stock_id,
                "stock_name": self.__stock_list[self.stock_id],
                "year": url_dict[title]["Year"],
                "report_type": report_type,
                "url": url_dict[title]["URL"]
            }
            self.report_list.append(report_info)

        self.rurl_list.clear()
        logging.info("released memory space from rurl_list")

    def __cycle_page(self, url, last_page):
        """
        Flip page in the report release webpage. Get the report's title and URL.
        The stop factor of this process depends on the latest year of all report in the database.

        **Note** - might rewrite this method with recursion
        """

        logging.info("start cycling page")
        page = 1

        while page < last_page:
            src = request(url.format(page))
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
        Get the title, URL, and the release date of the report, and return the stop factor of the page flipping process.
        """

        soup = BeautifulSoup(src, "lxml")
        titles = soup.find_all(string=re.compile(self.__title_pattern))
        flag = 0
        if not titles:
            return flag
        for title in titles:
            title_td = title.parent.parent
            url_td = title_td.next_sibling
            url = url_td.contents[0].attrs["href"]
            year = int(re.compile(r"(?P<year>\d{4})").search(str(title)).group("year"))
            if year >= self.__latest_year:
                if url not in self.__url_list:
                    flag += 1
                    self.rurl_list.append({str(title): {"Year": year, "URL": url}})
        if not flag:
            flag -= 1
        return flag

    def __handle(self):
        for stock_id in self.__stock_list.keys():
            logging.info("handling {}".format(stock_id))
            self.stock_id = stock_id

            src = request(_INIT_REQUEST.format(self.stock_id))

            (url, last_page) = get_page(src)

            self.__cycle_page(url, last_page)

            if self.rurl_list:
                self.__analy_rurl()
                logging.info("prepare to write {}".format(stock_id))

                for report_info in self.report_list:
                    self.__update(report_info)

                logging.info("{} new report are updated".format(len(self.report_list)))
                self.report_list.clear()
                logging.info("released memory space from report_list")

            logging.info("{} finished".format(stock_id))