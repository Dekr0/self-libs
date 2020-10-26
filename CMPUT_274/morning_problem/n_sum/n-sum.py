#!/usr/bin/env python
# -*- coding:utf-8 -*-

ns = [i for i in range(1, k+1)]
r = m
c = []

while True:
    if r - k > 0:
        r -= k
        c.append(k)
        k -= 1
        continue
    c.append(r)
    break

c.reverse()
print(len(c))
print(*c)