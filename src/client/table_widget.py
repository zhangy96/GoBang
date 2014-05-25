# -*- coding: utf-8 -*-
__author__ = 'zhangyang'

from PyQt4 import QtGui, QtCore
from ui.Ui_table_widget import Ui_table_widget
import sys


class TableWidget(QtGui.QWidget, Ui_table_widget):
    def __init__(self, parent=None):
        super(TableWidget, self).__init__(parent)
        self.setupUi(self)

    def paintEvent(self, event):
        opt = QtGui.QStyleOption()
        opt.init(self)
        painter = QtGui.QPainter(self)
        self.style().drawPrimitive(QtGui.QStyle.PE_Widget, opt, painter, self)