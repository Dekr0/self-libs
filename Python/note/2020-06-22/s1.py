#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import sys

base_logger = logging.getLogger("base_logger")
base_logger.setLevel(logging.DEBUG)

sub_logger = logging.getLogger("base_logger.sub_logger")

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

Filter = logging.Filter("base_filter")

formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)

base_logger.addHandler(handler)

base_logger.debug("debug msg")
base_logger.info("info msg")
base_logger.warning("warn msg")
sub_logger.error("debug msg")