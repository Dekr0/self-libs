#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
from os import path

sys.path.append(path.abspath(path.join(path.dirname(path.dirname(__file__)), "config")))
sys.path.append(path.abspath(path.join(path.dirname(path.dirname(__file__)), "libs")))


def main():

    if sys.argv == 2:
        site_name = sys.argv[1]
        sites = {

        }
        
    else:
        quit("Invalid parameters")


if __name__ == "__main__":
    main()
