#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

if __name__ == "__main__":
    dagparams = DefaultDagParams()
    result = dag(dagparams, ('wan', 'ke'), path_num=20)
    for item in result:
        print(item.score, item.path)
