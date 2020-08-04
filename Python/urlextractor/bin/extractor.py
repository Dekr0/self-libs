#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "libs"))
from libs import main_extractor

logging.basicConfig(filename="log.log",
                    format="%(asctime)s - %(levelname)s - %(module)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S %p",
                    level=logging.INFO)  # Setup basic config for a root logger

if __name__ == "__main__":
    logging.info("Script started\n")
    main_extractor.URLExtractor()  # initialize an instance of URLExtractor Class
    logging.info("Script finished\n")
