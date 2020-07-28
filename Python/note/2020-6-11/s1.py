#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy

np1 = numpy.array([1,2,3])
np2 = numpy.array([1.0, 2.0, 3.0])
np3 = numpy.array([[1.0, 2.0], [3.0, 4.0]])
np4 = numpy.array([[1,2], [3,4]], dtype=complex)

print(np1, np1.dtype)
print(np2, np2.dtype)
print(np3, np3.dtype)
print(np4, np4.dtype)