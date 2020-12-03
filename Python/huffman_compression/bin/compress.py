#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
from libs import main

if __name__ == "__main__":
    print(os.path.dirname(__name__))
    input()
    if len(sys.argv) < 2:
        print("Usage: drag and drop the file needed to compress (decompress) "
              "onto the .exe file")
        input()
    # else:
    #     sel = input().strip()
    #     if sel == "1":
    #         main.compress(sys.argv[1])
    #     elif sel == "2":
    #         if os.path.splitext(sys.argv[1])[-1] == ".huf":
    #             main.decompress(sys.argv[1])
    #         else:
    #             print("Failed to decompress: the given file does not end with "
    #                   ".huf")