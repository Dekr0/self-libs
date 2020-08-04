#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__name__)), "config"))
from config import config
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from win32com import client

adoconn = config.ADOCONNECTION
dsn = config.DSN

def connect():
    conn = client.Dispatch(adoconn)
    conn.Open(dsn)
    if conn.State == 1:
        return conn
    sys.exit(-2)



class Window(QMainWindow):

    def __init__(self, widgets):
        super(Window, self).__init__()

        self.setWindowTitle("Testing")
        self.resize(300, 50)

        self.setCentralWidget(widgets)


conn = connect()


class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        self.line_edit = QLineEdit()
        self.model = QStringListModel()
        self.completer = QCompleter()
        self.layout = QVBoxLayout()

        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setModel(self.model)
        self.model.setStringList(["1", "2", "3"])
        self.line_edit.setCompleter(self.completer)

        self.completer.highlighted.connect(self.block)
        self.completer.activated.connect(self.unblock)
        self.line_edit.textChanged.connect(self.changed)

        self.layout.addWidget(self.line_edit)

        self.setLayout(self.layout)

    @pyqtSlot()
    def block(self):
        print("block")
        print(self.line_edit.signalsBlocked())
        self.line_edit.blockSignals(True)
        print(self.line_edit.signalsBlocked())

    @pyqtSlot()
    def unblock(self):
        print("unblock")
        print(self.line_edit.signalsBlocked())
        self.line_edit.blockSignals(False)
        print(self.line_edit.signalsBlocked())

    @pyqtSlot()
    def changed(self):
        print("changed trig")
        text = self.line_edit.text().strip()
        if text:
            if len(re.findall("\d{1,6}", text)) == 1:
                field = "股票代码"
            else:
                field = "股票名称"
            self.add_stock(text, field)

    def add_stock(self, string, field):
        self.model.setStringList([])

        query = "SELECT * FROM 股票代码 WHERE {} LIKE '%{}%' ".format(field, string)

        (rs, result) = conn.Execute(query)
        stock_list = []

        while not rs.EOF:
            code = rs.Fields("股票代码").Value
            name = rs.Fields("股票名称").Value
            stock_list.append("{}-{}".format(code, name))
            rs.MoveNext()

        rs.Close()

        self.model.setStringList(stock_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    window = Window(widget)

    window.show()

    sys.exit(app.exec_())
