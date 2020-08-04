#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "libs"))
from libs import main_query


if __name__ == "__main__":
    main_query.ReportQuery()