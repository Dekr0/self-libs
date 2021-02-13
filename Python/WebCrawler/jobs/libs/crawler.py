#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
from os import path
sys.path.append(path.abspath(path.join(path.dirname(path.dirname(__file__)), "config")))

from config.config import *


class BaseCrawler:

    def __init__(self, url):
        self.url = url


class IndeedCrawler(BaseCrawler):

    def __init__(self, query, location):

        super(IndeedCrawler, self).__init__(_URLS["indeed"])

        self.query = query
        self.location = location
        self.


class JobBankCrawler(BaseCrawler):

    pass