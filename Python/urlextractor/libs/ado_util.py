"""

Provide method to access table and data in the database

"""

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from win32com import client
from config.config import *
from config.ADOConstants import *
import socketserver


_ADOCONNECTION = ADOCONNECTION
_ADODBCOMMAND = ADODBCOMMAND
_DATABASE = DATABASE
_DSN = DSN


class ADOUtil(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(ADOUtil, "_instance"):
            ADOUtil._instance = object.__new__(cls)
        return ADOUtil._instance

    def __init__(self):
        self.__get_conn()

        self.get_report_type = self.__get_report_type
        self.get_command = self.__get_command
        self.get_latest_year = self.__get_latest_year
        self.get_stock_id = self.__get_stock_id
        self.get_url_list = self.__get_url_list

    def __get_conn(self):
        if not hasattr(self, "conn"):
            try:
                conn = client.Dispatch(_ADOCONNECTION)
                conn.Open(_DSN)
                if not conn.State == adStateOpen:
                    raise Exception

                self.conn = conn
            except Exception as ex:
                sys.exit("Failed to connect ot database: {}".format(ex))

    def __get_command(self):
        """
        Create an modified ADO Command object with unfilled, customized parameters for insert data into the database.
        """

        if not hasattr(self, "cmd") or not hasattr(self, "params"):
            self.cmd = client.Dispatch(_ADODBCOMMAND)
            self.cmd.ActiveConnection = self.conn  # Attach to an ADO Connection object instance
            self.cmd.CommandType = adCmdText  # Type of command being used

            # "?" servers as a placeholder for a customized parameter
            query = "INSERT INTO PDF网址(股票代码, 股票名称, 年度, 报告编号, 网址) VALUES (?, ?, ?, ?, ?)"
            self.cmd.CommandText = query

            # A dictionary that stores the ADO Parameter object instance
            self.params = dict()

            # Create Parameter object instances and setup their properties
            self.params["stock_id"] = self.cmd.CreateParameter("stock_id", adVarChar, adParamInput, 1024)
            self.params["stock_name"] = self.cmd.CreateParameter("stock_name", adVarChar, adParamInput, 1024)
            self.params["year"] = self.cmd.CreateParameter("year", adInteger, adParamInput)
            self.params["report_type"] = self.cmd.CreateParameter("report_type", adInteger, adParamInput)
            self.params["url"] = self.cmd.CreateParameter("url", adVarChar, adParamInput, 1024 * 4)
            self.params["year"].NumericScale = 0
            self.params["report_type"].NumericScale = 0

            # Attach the Parameter object instance to an Command object instance
            for i in self.params.keys():
                self.cmd.Parameters.Append(self.params[i])
            self.cmd.Prepared = True

        return self.cmd, self.params

    def __get_latest_year(self):
        if not hasattr(self, "latest_year"):
            query = "SELECT MAX(年度) AS latest_year FROM PDF网址"
            (rs, result) = self.conn.Execute(query)
            self.latest_year = int(rs.Fields("latest_year").Value)
            rs.Close()

        return self.latest_year

    def __get_stock_id(self):
        if not hasattr(self, "stock_id"):
            self.stock_id = dict()
            query = "SELECT 股票代码, 股票名称 FROM 股票代码"
            (rs, result) = self.conn.Execute(query)

            while not rs.EOF:
                self.stock_id[rs.Fields("股票代码").Value] = rs.Fields("股票名称").Value
                rs.MoveNext()
            rs.Close()

        return self.stock_id

    def __get_report_type(self):
        if not hasattr(self, "report_type"):
            self.report_type = dict()
            query = "SELECT * FROM 报告类型"
            (rs, result) = self.conn.Execute(query)

            while not rs.EOF:
                self.report_type[rs.Fields("报告类型").Value] = int(rs.Fields("报告编码").Value)
                rs.MoveNext()
            rs.Close()

        return self.report_type

    def __get_url_list(self):
        if not hasattr(self, "url_list"):
            query = "SELECT * FROM PDF网址"
            (rs, result) = self.conn.Execute(query)
            self.url_list = []

            while not rs.EOF:
                url = rs.Fields("网址").Value
                self.url_list.append(url)
                rs.MoveNext()

        return self.url_list
