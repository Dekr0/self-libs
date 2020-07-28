#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re


def showResult(matchObjs):
    for matchObj in matchObjs:
        print(matchObj)
    print("\n")


DoubledWords = "Pairs in the the spring.\n" \
               "The theoretical viewpoint is of little value here.\n" \
               "I view the theoretical viewpoint as being of little value here.\n" \
               "I think that that is often overdone.\n" \
               "This sentence contains contains a doubled word or two two.\n" \
               "Fear fear is a fearful thing.\n" \
               "Writing successful programs requires that the the programmer fully understands the problem to be " \
               "solved. "

pat = re.compile(r"\b([A-Za-z]+) +\1\b")
matches = pat.finditer(DoubledWords)
showResult(matches)
