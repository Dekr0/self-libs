#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "libs"))
from libs.crawler import URLCrawler

logging.basicConfig(filename="extractor_log.log",
                    format="%(asctime)s - %(levelname)s - %(module)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S %p",
                    level=logging.INFO)

if __name__ == "__main__":
    print("搜索脚本运行中...")
    logging.info("Script started\n")
    URLCrawler()
    logging.info("Script finished\n")
