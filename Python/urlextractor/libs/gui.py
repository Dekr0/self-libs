#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import sys
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def show(conn, report_dict):
    app = QApplication(sys.argv)
    framework = Framework(conn, report_dict)
    window = QueryWindow(framework)

    window.show()

    sys.exit(app.exec_())


class QueryWindow(QMainWindow):

    def __init__(self, widgets):
        super(QueryWindow, self).__init__()

        self.setWindowTitle("Report Query")
        self.resize(250, 100)

        self.setCentralWidget(widgets)


class SelectionWindow(QMainWindow):

    def __init__(self, url_list):
        super(SelectionWindow, self).__init__()



class ErrorEvents(Exception):
    error_dict = {
        "40": "股票代码和股票名称输入处不可为空",
        "41": "所输入的股票代码和股票名称不符合查询格式",
        "42": "年度输入处不可为空",
        "43": "查询结果不存在"
    }

    def __init__(self, flag):
        self.msg = ErrorEvents.error_dict[flag]


class Framework(QWidget):

    def __init__(self, conn, report_dict):
        super(Framework, self).__init__()

        self.conn = conn
        self.report_dict = report_dict

        self.__init_completer()
        self.__init_stock_input()
        self.__init_year_input()
        self.__init_type_selection(report_dict)
        self.button = QPushButton("查询")
        self.layout = QVBoxLayout()

        self.button.clicked.connect(self.query)

        self.layout.addWidget(self.stock_box)
        self.layout.addWidget(self.year_box)
        self.layout.addWidget(self.type_box)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def __init_completer(self):
        self.completer = QCompleter()
        self.model = QStringListModel()

        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setModel(self.model)

        self.completer.activated.connect(self.unblock)
        self.completer.highlighted.connect(self.block)

    def __init_stock_input(self):
        self.stock_box = QGroupBox("股票代码和股票名称")
        self.stock_layout = QHBoxLayout()
        self.stock_input = QLineEdit()

        self.stock_input.setCompleter(self.completer)
        self.stock_input.textChanged.connect(self.search_factor)

        self.stock_layout.addWidget(self.stock_input)

        self.stock_box.setLayout(self.stock_layout)

    def __init_year_input(self):
        self.year_box = QGroupBox("年度")
        self.year_layout = QHBoxLayout()
        self.year_input = QLineEdit()

        self.year_input.setValidator(QRegExpValidator(QRegExp("\d{0,4}")))

        self.year_layout.addWidget(self.year_input)

        self.year_box.setLayout(self.year_layout)

    def __init_type_selection(self, report_dict):
        self.type_box = QGroupBox("报告类型")
        self.type_layout = QHBoxLayout()
        self.type_combobox = QComboBox()

        self.type_combobox.addItems(report_dict.keys())

        self.type_layout.addWidget(self.type_combobox)

        self.type_box.setLayout(self.type_layout)

    def __add_stock(self, iterable):
        self.model.setStringList(iterable)

    @pyqtSlot()
    def block(self):
        if not self.stock_input.signalsBlocked():
            self.stock_input.blockSignals(True)

    @pyqtSlot()
    def unblock(self):
        if self.stock_input.signalsBlocked():
            self.stock_input.blockSignals(False)
            self.model.setStringList([])

    @pyqtSlot()
    def search_factor(self):
        text = self.stock_input.text().strip()
        if text:
            if re.fullmatch("\d{1,6}", text):
                self.default_search(text, "股票代码")
            elif re.fullmatch("[a-zA-Z ]+", text):
                self.pinyin_search(text)
            else:
                self.default_search(text, "股票名称")

    @pyqtSlot()
    def query(self):
        stock = self.stock_input.text().strip()
        year = self.year_input.text().strip()
        try:
            if not stock:
                raise ErrorEvents("40")
            if not re.fullmatch("\d{6}-[\w ]+", stock):
                raise ErrorEvents("41")
            if not year:
                raise ErrorEvents("42")

            (code, name) = stock.split("-")
            report_type = self.report_dict[self.type_combobox.currentText()]

            query = r"SELECT * FROM PDF网址 WHERE 股票代码='{}'AND 股票名称='{}' AND 年度={} AND 报告编号={}".format(code
                                                                                                     , name, int(year),
                                                                                                     report_type)
            cquery = r"SELECT COUNT(*) AS 数量 FROM ({})".format(query)
            (com, result) = self.conn.Execute(cquery)
            count = com.Fields("数量").Value
            com.Close()

            if not count:
                raise ErrorEvents("43")

            (rs, result) = self.conn.Execute(query)
            url_list = []
            while not rs.EOF:
                url_list.append(rs.Fields("网址").Value)
                rs.MoveNext()

            rs.Close()

        except ErrorEvents as ex:
            QMessageBox.about(self, "查询错误", ex.msg)

    def default_search(self, string, flag):
        query = r"SELECT * FROM 股票代码 WHERE {} LIKE '%{}%'".format(flag, string)
        stock_list = []

        (rs, result) = self.conn.Execute(query)
        while not rs.EOF:
            code = rs.Fields("股票代码").Value
            name = rs.Fields("股票名称").Value
            stock_list.append("{}-{}".format(code, name))
            rs.MoveNext()

        rs.Close()

        self.__add_stock(stock_list)

    def pinyin_search(self, string):
        pass
