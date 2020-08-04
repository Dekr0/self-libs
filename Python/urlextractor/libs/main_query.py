#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__name__)), "config"))
from libs.gui import show
from config.config import *
from config.ADOConstants import *
from win32com import client

_ADOCONNECTION = ADOCONNECTION
_CONNS = []
_DSN = DSN


def __get_conn():
    """
    Initialize a connection object which hold the connection with the database. Only one connection object is allowed
    :return:
    """

    if not _CONNS:
        try:
            conn = client.Dispatch(_ADOCONNECTION)
            conn.Open(_DSN)
            if conn.State == adStateOpen:  # Check whether the connection is open
                _CONNS.append(conn)

                return _CONNS[0]

            raise Exception
        except Exception as ex:
            sys.exit("Failed to connect ot database: {}".format(ex))

    return _CONNS[0]


def __get_report_type(conn):
    """
    Get the name of each report type and its corresponded id, and store them in a dictionary. Keys will be the name of
    the report type; Value will be the id of the report type.
    :param conn:
    :return:
    """

    rt = dict()
    query = "SELECT * FROM 报告类型"
    (rs, result) = conn.Execute(query)

    while not rs.EOF:
        rt[rs.Fields("报告类型").Value] = int(rs.Fields("报告编码").Value)
        rs.MoveNext()

    rs.Close()

    return rt


def singleton(cls, *args, **kwargs):
    _instance = []

    def _singleton():
        if not _instance:
            _instance.append(cls(*args, **kwargs))
        return _instance[0]

    return _singleton


_CONN = __get_conn()
REPORT_TYPE = __get_report_type(_CONN)

@singleton
class ReportQuery:

    def __init__(self):
        self.__handle()

    def __handle(self):
        show(_CONN, REPORT_TYPE)
