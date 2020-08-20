#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import sys
from os import path

sys.path.append(path.abspath(path.join(path.dirname(path.dirname(__file__)), "libs")))
from libs.crawler import URLCrawler

logging.basicConfig(filename="url_crawler_log.log",
                    format="%(asctime)s - %(levelname)s - %(module)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S %p",
                    level=logging.INFO)

if __name__ == "__main__":
    print("搜索脚本运行中...")
    logging.info("Script started\n")
    URLCrawler()
    logging.info("Script finished\n")
