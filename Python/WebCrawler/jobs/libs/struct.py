#!/usr/bin/env python
# -*- coding:utf-8 -*-


class JobInstance:

    def __init__(self, title, company, location, *kwargs):
        self.title = title
        self.company = company
        self.location  = location