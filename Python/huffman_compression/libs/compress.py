#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import main

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: drag and drop the file needed to compress (decompress) "
              "onto the .exe file")
    else:
        sel = input("1. Compression\n2. Decompression\n").strip()
        if sel == "1":
            main.compress(sys.argv[1])
        elif sel == "2":
            if os.path.splitext(sys.argv[1])[-1] == ".huf":
                main.decompress(sys.argv[1])
            else:
                print("Failed to decompress: the given file does not end with "
                      ".huf")