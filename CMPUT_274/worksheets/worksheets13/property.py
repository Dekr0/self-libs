#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
When to make a attribute / method as public or private (depend on implementation)
    - will the value be needed by the users of the class
    - no, private
Uses of property to set up setter and getter
Not ideal way to design such a class
    - "drowned" with mainly unnecessary - methods or properties
    - many attributes are only internally needed and creating interfaces for
      the user of the class increases unnecessarily the usability of the class
When to create setter / getter / property
    -
"""


class P_1:
    """
    Pythonic way
    """

    def __init__(self, x):
        self.x = x  # invoke setter x (because of assignment?)

    @property  # decorator property
    def x(self):
        return self.__x

    @x.setter  # decorating by property x, set x (one below) as the setter of property x
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


class P_2:
    """
    Equivalent to P_1
    """

    def __init__(self, x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(__get_x, __set_x)
    # create an new instance of property, with getter, __get_x, and setter, __set_x


p1 = P(1001)
print(p1.x)  # invoke property x
