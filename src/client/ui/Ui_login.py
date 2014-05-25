# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PyCharm_Project\GoBang\src\client\ui\login.ui'
#
# Created: Mon May 19 15:49:20 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName(_fromUtf8("login_window"))
        login_window.resize(381, 282)
        login_window.setStyleSheet(_fromUtf8(""))
        self.verticalLayout_3 = QtGui.QVBoxLayout(login_window)
        self.verticalLayout_3.setMargin(5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.min_btn = QtGui.QPushButton(login_window)
        self.min_btn.setMinimumSize(QtCore.QSize(27, 22))
        self.min_btn.setMaximumSize(QtCore.QSize(27, 22))
        self.min_btn.setStyleSheet(_fromUtf8("QPushButton#min_btn{\n"
"border-image: url(:/img/min.png);\n"
"background-color: transparent;\n"
"}\n"
"QPushButton#min_btn::hover{\n"
"background-image: url(:/img/min_hover.png);\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton#min_btn::pressed{\n"
"background-image: url(:/img/min_pressed.png);\n"
"background-color: transparent;\n"
"}\n"
""))
        self.min_btn.setText(_fromUtf8(""))
        self.min_btn.setObjectName(_fromUtf8("min_btn"))
        self.horizontalLayout_2.addWidget(self.min_btn)
        self.close_btn = QtGui.QPushButton(login_window)
        self.close_btn.setMinimumSize(QtCore.QSize(27, 22))
        self.close_btn.setMaximumSize(QtCore.QSize(27, 22))
        self.close_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
"border-image: url(:/img/close.png);\n"
"background-color: transparent;\n"
"}\n"
"QPushButton::hover{\n"
"background-image: url(:/img/close_hover.png);\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-image: url(:/img/close_pressed.png);\n"
"background-color: transparent;\n"
"}\n"
""))
        self.close_btn.setText(_fromUtf8(""))
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.horizontalLayout_2.addWidget(self.close_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 20)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(login_window)
        self.widget.setMinimumSize(QtCore.QSize(67, 67))
        self.widget.setMaximumSize(QtCore.QSize(67, 67))
        self.widget.setStyleSheet(_fromUtf8("border-image: url(:/img/AppID8.png) stretch;"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ip_edit = QtGui.QLineEdit(login_window)
        self.ip_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.ip_edit.setAccessibleDescription(_fromUtf8(""))
        self.ip_edit.setText(_fromUtf8(""))
        self.ip_edit.setObjectName(_fromUtf8("ip_edit"))
        self.horizontalLayout_3.addWidget(self.ip_edit)
        self.port_edit = QtGui.QLineEdit(login_window)
        self.port_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.port_edit.setObjectName(_fromUtf8("port_edit"))
        self.horizontalLayout_3.addWidget(self.port_edit)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.name_edit = QtGui.QLineEdit(login_window)
        self.name_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.name_edit.setObjectName(_fromUtf8("name_edit"))
        self.verticalLayout.addWidget(self.name_edit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.login_btn = QtGui.QPushButton(login_window)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QtCore.QSize(151, 30))
        self.login_btn.setStyleSheet(_fromUtf8("QPushButton#login_btn{\n"
"border-width:5px;\n"
"border-image: url(:/img/pushbutton.png) 5 5 5 5;\n"
"}\n"
"\n"
"QPushButton#login_btn::hover{\n"
"border-width:5px;\n"
"border-image: url(:/img/pushbutton_hover.png) 5 5 5 5;\n"
"}\n"
"\n"
"QPushButton#login_btn::pressed{\n"
"border-width:5px;\n"
"border-image: url(:/img/pushbutton_pressed.png) 5 5 5 5;\n"
"}"))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.verticalLayout_2.addWidget(self.login_btn)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        self.ip_edit.setPlaceholderText(_translate("login_window", "IP:(localhost default)", None))
        self.port_edit.setPlaceholderText(_translate("login_window", "Port:12345", None))
        self.name_edit.setPlaceholderText(_translate("login_window", "Nick Name", None))
        self.login_btn.setText(_translate("login_window", "log in", None))

import img_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    login_window = QtGui.QDialog()
    ui = Ui_login_window()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec_())

