# -*- coding: utf-8 -*-
__author__ = 'gzs2473'

from PyQt4 import QtCore, QtGui

from ui.Ui_login import Ui_login_window
from custom_dialog import CustomDialog


class LoginWindow(CustomDialog, Ui_login_window):
    login_signal = QtCore.pyqtSignal(str, int, str)
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setTexture(u":/img/login_skin.png")

        self.setupUi(self)
        self.__beautify()
        self.__connect_slots()

    ###########################################################
    #美化控件
    ###########################################################
    def __beautify(self):
        self.min_btn.setAutoDefault(False)
        self.close_btn.setAutoDefault(False)
        self.ip_edit.setFont(QtGui.QFont(u"微软雅黑", 10))
        self.ip_edit.setText(u"127.0.0.1")
        self.port_edit.setFont(QtGui.QFont(u"微软雅黑", 10))
        self.port_edit.setText(u"12345")
        self.name_edit.setFont(QtGui.QFont(u"微软雅黑", 10))
        self.name_edit.setToolTip(u"取个昵称,昵称要唯一")
        self.name_edit.setFocus()
        self.login_btn.setFont(QtGui.QFont(u"微软雅黑", 10))

    ###########################################################
    #连接信号与槽
    ###########################################################
    def __connect_slots(self):
        self.login_btn.clicked.connect(self.login)
        self.close_btn.clicked.connect(self.close)
        self.min_btn.clicked.connect(self.showMinimized)

    ###########################################################
    #点击登录按钮，执行此方法
    ###########################################################
    @QtCore.pyqtSlot()
    def login(self):
        host = self.ip_edit.text()
        port = int(self.port_edit.text())
        name = self.name_edit.text()
        if not name:
            print 'nick name expected!'
            return

        if not host:
            host = '127.0.0.1'
        if not port:
            port = 12345

        self.login_signal.emit(host, port, name)

