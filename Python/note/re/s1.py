#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
匹配IP地址

1. IP地址中包含的数值最大不能超过255
2. 一位数字，位于0~9之间的一个数字：[0-9]
3. 两位数字，范围是10~99：[1-9][0-9]（之所以用[1-9]而不是[0-9]，因为小于10的数字属于一位数。第二位书可以是0）
4. 三位数字（分步骤）
       a. 匹配100~199之间的三位数：1[0-9][0-9]
       b. 匹配200~249之间的三位数：2[0-4][0-9]
       c. 匹配259~255之间的三位数：25[0-5]

定义：
1. 如果是一位数，匹配任何0~9的数字
2. 如果是两位数，匹配第一个字符为1~9且第二个字符为0~9的数字
3. 如果是三位数，那么与下面任一项匹配即可：
       a. 匹配数字1，后跟一个数字0~9，后跟一个数字0~9；
       b. 匹配数字2，后跟一个数字0~4，后跟一个数字0~9；
       c. 匹配数字2，后跟一个数字5，后跟一个数字0~5。

([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])存在问题，当与IP地址进行匹配时，256被匹配到。
单独匹配256时，第一个数字2被匹配了，即256中的2与圆括号中的第一个选项匹配[0-9]。同样的，5和6也会被匹配。
实际上那是三次独立的匹配。

当表达式包含”|“（或）字符，如果其中一个选项被匹配到，其余的选项将会被忽略，因为这个整个组件被匹配成功

"""

import re


def showResult(matchObjs):
    for matchObj in matchObjs:
        print(matchObj)
    print("\n")


# IP = "\n12.12.12.12\n" \
#      "255.255.256.255\n" \
#      "12.255.12.255\n" \
#      "256.123.256.123\n" \
#      "8.234.88.55\n" \
#      "196.83.83.191\n" \
#      "8.234.88,55\n" \
#      "88.173.71.66\n" \
#      "241.92.88.103"

# DATE = "2004-12-31\n" \
#        "2001/09/11\n" \
#        "2003.11.19\n" \
#        "2002/04/29\n" \
#        "2000/10/19\n" \
#        "2005/08/28\n" \
#        "2006/09/18\n" \
#        "2000/13/36\n" \
#        "2000/24/41"

# dollar = "The pound, ..., and US dollar, $, are major global currencies\n" \
#          "\n" \
#          "$ 99.00\n" \
#          "\n" \
#          "99,00 $\n" \
#          "$1,000,000\n" \
#          "\n" \
#          "$1000\n" \
#          "\n" \
#          "$1,000.00\n" \
#          "\n" \
#          "$0.50\n" \
#          "\n" \
#          "$2 # A Perl variable\n" \
#          "\n" \
#          "$ 0.99\n" \
#          "\n" \
#          "$myVariable\n" \
#          "\n" \
#          "$2.25" \

text = "ABC DEF GHI\n" \
       "GHI ABC DEF\n" \
       "ABC DEF GHI\n" \
       "CAB CBA AAA"

# pattern = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$")
# matches = pattern.finditer(IP)
# pattern = re.compile("\$[0-9]+\.?[0-9]*", flags=re.MULTILINE)
# matches = pattern.finditer(dollar)
pattern = re.compile(r"\bA")
matches = pattern.finditer(text)
showResult(matches)
