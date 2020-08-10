#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "libs"))
from libs.query import ReportQuery


logging.basicConfig(filename="query_log.log",
                    format="%(asctime)s - %(levelname)s - %(module)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S %p",
                    level=logging.INFO)


if __name__ == "__main__":
    logging.info("Script started")
    ReportQuery()
