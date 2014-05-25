# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PyCharm_Project\GoBang\src\client\ui\table_widget.ui'
#
# Created: Tue May 20 15:17:32 2014
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

class Ui_table_widget(object):
    def setupUi(self, table_widget):
        table_widget.setObjectName(_fromUtf8("table_widget"))
        table_widget.resize(119, 121)
        table_widget.setMinimumSize(QtCore.QSize(119, 121))
        table_widget.setMaximumSize(QtCore.QSize(119, 121))
        table_widget.setStyleSheet(_fromUtf8(""))
        self.horizontalLayout = QtGui.QHBoxLayout(table_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.left_btn = QtGui.QPushButton(table_widget)
        self.left_btn.setMinimumSize(QtCore.QSize(32, 32))
        self.left_btn.setMaximumSize(QtCore.QSize(32, 32))
        self.left_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color:transparent;\n"
"}\n"
"QPushButton::hover{\n"
"border: 1px solid rgba(255,255,255,100);\n"
"background-color:transparent;\n"
"}"))
        self.left_btn.setText(_fromUtf8(""))
        self.left_btn.setObjectName(_fromUtf8("left_btn"))
        self.horizontalLayout.addWidget(self.left_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.right_btn = QtGui.QPushButton(table_widget)
        self.right_btn.setMinimumSize(QtCore.QSize(32, 32))
        self.right_btn.setMaximumSize(QtCore.QSize(32, 32))
        self.right_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color:transparent;\n"
"}\n"
"QPushButton::hover{\n"
"border: 1px solid rgba(255,255,255,100);\n"
"background-color:transparent;\n"
"}"))
        self.right_btn.setText(_fromUtf8(""))
        self.right_btn.setObjectName(_fromUtf8("right_btn"))
        self.horizontalLayout.addWidget(self.right_btn)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(table_widget)
        QtCore.QMetaObject.connectSlotsByName(table_widget)

    def retranslateUi(self, table_widget):
        table_widget.setWindowTitle(_translate("table_widget", "Form", None))

import img_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    table_widget = QtGui.QWidget()
    ui = Ui_table_widget()
    ui.setupUi(table_widget)
    table_widget.show()
    sys.exit(app.exec_())

