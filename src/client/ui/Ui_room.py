# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PyCharm_Project\GoBang\src\client\ui\room.ui'
#
# Created: Fri May 23 15:16:18 2014
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

class Ui_room_window(object):
    def setupUi(self, room_window):
        room_window.setObjectName(_fromUtf8("room_window"))
        room_window.resize(1021, 640)
        room_window.setWindowTitle(_fromUtf8(""))
        room_window.setStyleSheet(_fromUtf8("QScrollBar{\n"
"background:white;\n"
"  width: 10px;\n"
"}\n"
"QScrollBar::handle{\n"
"background:rgb(180, 180, 180, 150);\n"
"}\n"
"QScrollBar::handle:hover{\n"
"background:rgb(150, 150, 150, 180);\n"
"}\n"
"QScrollBar::add-page{\n"
"background:transparent;\n"
"}\n"
"QScrollBar::sub-page{\n"
"background:transparent; \n"
"}\n"
"QScrollBar::sub-line{\n"
"background:transparent;\n"
"}\n"
"QScrollBar::add-line{\n"
"background:transparent;\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(room_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.title_label = QtGui.QLabel(room_window)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.horizontalLayout.addWidget(self.title_label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.min_btn = QtGui.QPushButton(room_window)
        self.min_btn.setMinimumSize(QtCore.QSize(27, 22))
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
        self.horizontalLayout.addWidget(self.min_btn)
        self.close_btn = QtGui.QPushButton(room_window)
        self.close_btn.setMinimumSize(QtCore.QSize(27, 22))
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
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(5, 2, -1, 5)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.icon_label = QtGui.QLabel(room_window)
        self.icon_label.setMinimumSize(QtCore.QSize(66, 67))
        self.icon_label.setMaximumSize(QtCore.QSize(66, 67))
        self.icon_label.setStyleSheet(_fromUtf8("background-image: url(:/img/AppID8.png);"))
        self.icon_label.setText(_fromUtf8(""))
        self.icon_label.setObjectName(_fromUtf8("icon_label"))
        self.horizontalLayout_2.addWidget(self.icon_label)
        self.count_label = QtGui.QLabel(room_window)
        self.count_label.setObjectName(_fromUtf8("count_label"))
        self.horizontalLayout_2.addWidget(self.count_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.info_widget = QtGui.QWidget(room_window)
        self.info_widget.setStyleSheet(_fromUtf8("QWidget#info_widget{\n"
"background:rgba(255,255,255,100);\n"
"}"))
        self.info_widget.setObjectName(_fromUtf8("info_widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.info_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(20, 5, 20, 5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.name_label = QtGui.QLabel(self.info_widget)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.verticalLayout_3.addWidget(self.name_label)
        self.record_label = QtGui.QLabel(self.info_widget)
        self.record_label.setObjectName(_fromUtf8("record_label"))
        self.verticalLayout_3.addWidget(self.record_label)
        self.score_label = QtGui.QLabel(self.info_widget)
        self.score_label.setObjectName(_fromUtf8("score_label"))
        self.verticalLayout_3.addWidget(self.score_label)
        self.horizontalLayout_2.addWidget(self.info_widget)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.content_widget = QtGui.QWidget(room_window)
        self.content_widget.setStyleSheet(_fromUtf8("QWidget#content_widget{\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}\n"
""))
        self.content_widget.setObjectName(_fromUtf8("content_widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.content_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(5)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.left_widget = QtGui.QWidget(self.content_widget)
        self.left_widget.setMinimumSize(QtCore.QSize(0, 480))
        self.left_widget.setStyleSheet(_fromUtf8("QWidget#left_widget{\n"
"background-color: rgb(81, 113, 158);\n"
"}"))
        self.left_widget.setObjectName(_fromUtf8("left_widget"))
        self.gridLayout = QtGui.QGridLayout(self.left_widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3.addWidget(self.left_widget)
        self.right_widget = QtGui.QWidget(self.content_widget)
        self.right_widget.setMinimumSize(QtCore.QSize(322, 0))
        self.right_widget.setMaximumSize(QtCore.QSize(322, 16777215))
        self.right_widget.setObjectName(_fromUtf8("right_widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.right_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tab_widget = QtGui.QWidget(self.right_widget)
        self.tab_widget.setMinimumSize(QtCore.QSize(0, 30))
        self.tab_widget.setStyleSheet(_fromUtf8("QWidget#tab_widget{\n"
"border-width: 5px;\n"
"border-image: url(:/img/TitleBack.png)5 5 5 5;\n"
"}"))
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.tab_widget)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.players_btn = QtGui.QPushButton(self.tab_widget)
        self.players_btn.setMinimumSize(QtCore.QSize(70, 25))
        self.players_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
"border-width:5px;\n"
"border-image: url(:/img/pushbutton.png) 5 5 5 5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-width:5px;\n"
"border-image: url(:/img/pushbutton_hover.png) 5 5 5 5;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"border-width:5px;\n"
"border-image: url(:/img/pushbutton_pressed.png) 5 5 5 5;\n"
"}"))
        self.players_btn.setObjectName(_fromUtf8("players_btn"))
        self.horizontalLayout_7.addWidget(self.players_btn)
        self.rank_btn = QtGui.QPushButton(self.tab_widget)
        self.rank_btn.setMinimumSize(QtCore.QSize(70, 25))
        self.rank_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
"border-width:5px;\n"
"border-image: url(:/img/pushbutton.png) 5 5 5 5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-width:5px;\n"
"border-image: url(:/img/pushbutton_hover.png) 5 5 5 5;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"border-width:5px;\n"
"border-image: url(:/img/pushbutton_pressed.png) 5 5 5 5;\n"
"}"))
        self.rank_btn.setObjectName(_fromUtf8("rank_btn"))
        self.horizontalLayout_7.addWidget(self.rank_btn)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addWidget(self.tab_widget)
        self.stackedWidget = QtGui.QStackedWidget(self.right_widget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.player_list = QtGui.QListWidget(self.page)
        self.player_list.setStyleSheet(_fromUtf8("QListWidget{\n"
"border:0px;\n"
"}\n"
"QListWidget::item{\n"
"height:30px;\n"
"selection-background-color:lightblue;\n"
"}\n"
""))
        self.player_list.setAlternatingRowColors(True)
        self.player_list.setObjectName(_fromUtf8("player_list"))
        self.horizontalLayout_5.addWidget(self.player_list)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.rank_1 = QtGui.QLabel(self.page_2)
        self.rank_1.setMinimumSize(QtCore.QSize(40, 40))
        self.rank_1.setStyleSheet(_fromUtf8("background:white;"))
        self.rank_1.setText(_fromUtf8(""))
        self.rank_1.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/00090.png")))
        self.rank_1.setObjectName(_fromUtf8("rank_1"))
        self.verticalLayout_2.addWidget(self.rank_1)
        self.rank_2 = QtGui.QLabel(self.page_2)
        self.rank_2.setMinimumSize(QtCore.QSize(40, 40))
        self.rank_2.setStyleSheet(_fromUtf8("background:white;"))
        self.rank_2.setText(_fromUtf8(""))
        self.rank_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/00091.png")))
        self.rank_2.setObjectName(_fromUtf8("rank_2"))
        self.verticalLayout_2.addWidget(self.rank_2)
        self.rank_3 = QtGui.QLabel(self.page_2)
        self.rank_3.setMinimumSize(QtCore.QSize(40, 40))
        self.rank_3.setStyleSheet(_fromUtf8("background:white;"))
        self.rank_3.setText(_fromUtf8(""))
        self.rank_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/00092.png")))
        self.rank_3.setObjectName(_fromUtf8("rank_3"))
        self.verticalLayout_2.addWidget(self.rank_3)
        self.rank_4 = QtGui.QLabel(self.page_2)
        self.rank_4.setMinimumSize(QtCore.QSize(40, 40))
        self.rank_4.setStyleSheet(_fromUtf8("background:white;"))
        self.rank_4.setAlignment(QtCore.Qt.AlignCenter)
        self.rank_4.setObjectName(_fromUtf8("rank_4"))
        self.verticalLayout_2.addWidget(self.rank_4)
        self.rank_5 = QtGui.QLabel(self.page_2)
        self.rank_5.setMinimumSize(QtCore.QSize(0, 40))
        self.rank_5.setStyleSheet(_fromUtf8("background:white;"))
        self.rank_5.setAlignment(QtCore.Qt.AlignCenter)
        self.rank_5.setObjectName(_fromUtf8("rank_5"))
        self.verticalLayout_2.addWidget(self.rank_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.rank_table = QtGui.QTableWidget(self.page_2)
        self.rank_table.setStyleSheet(_fromUtf8("border:0px;\n"
"selection-background-color:lightblue;"))
        self.rank_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.rank_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.rank_table.setShowGrid(False)
        self.rank_table.setRowCount(5)
        self.rank_table.setColumnCount(2)
        self.rank_table.setObjectName(_fromUtf8("rank_table"))
        self.rank_table.horizontalHeader().setVisible(False)
        self.rank_table.horizontalHeader().setDefaultSectionSize(100)
        self.rank_table.horizontalHeader().setStretchLastSection(True)
        self.rank_table.verticalHeader().setVisible(False)
        self.rank_table.verticalHeader().setDefaultSectionSize(40)
        self.rank_table.verticalHeader().setHighlightSections(True)
        self.horizontalLayout_6.addWidget(self.rank_table)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.line = QtGui.QFrame(self.right_widget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.textBrowser = QtGui.QTextBrowser(self.right_widget)
        self.textBrowser.setStyleSheet(_fromUtf8("border:0px;"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.chat_widget = QtGui.QWidget(self.right_widget)
        self.chat_widget.setMinimumSize(QtCore.QSize(0, 41))
        self.chat_widget.setStyleSheet(_fromUtf8("QWidget#chat_widget{\n"
"border-image: url(:/img/myexpression.bmp);\n"
"}"))
        self.chat_widget.setObjectName(_fromUtf8("chat_widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.chat_widget)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEdit = QtGui.QLineEdit(self.chat_widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.send_btn = QtGui.QPushButton(self.chat_widget)
        self.send_btn.setMinimumSize(QtCore.QSize(24, 23))
        self.send_btn.setStyleSheet(_fromUtf8("QPushButton#send_btn{\n"
"    border-image: url(:/img/send.png)0 46 0 0;\n"
"}\n"
"QPushButton#send_btn::hover{\n"
"    border-image: url(:/img/send.png)0 23 0 23;\n"
"}\n"
"QPushButton#send_btn::pressed{\n"
"    border-image: url(:/img/send.png)0 0 0 46;\n"
"}"))
        self.send_btn.setText(_fromUtf8(""))
        self.send_btn.setObjectName(_fromUtf8("send_btn"))
        self.horizontalLayout_4.addWidget(self.send_btn)
        self.verticalLayout_4.addWidget(self.chat_widget)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(3, 3)
        self.horizontalLayout_3.addWidget(self.right_widget)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addWidget(self.content_widget)

        self.retranslateUi(room_window)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), room_window.close)
        QtCore.QMetaObject.connectSlotsByName(room_window)

    def retranslateUi(self, room_window):
        self.title_label.setText(_translate("room_window", "gobang made by 9527", None))
        self.count_label.setText(_translate("room_window", "total person", None))
        self.name_label.setText(_translate("room_window", "Never More", None))
        self.record_label.setText(_translate("room_window", "胜：5 平：5 负：5 胜率：33%", None))
        self.score_label.setText(_translate("room_window", "积分：10", None))
        self.players_btn.setText(_translate("room_window", "players", None))
        self.rank_btn.setText(_translate("room_window", "rank", None))
        self.rank_4.setText(_translate("room_window", "4", None))
        self.rank_5.setText(_translate("room_window", "5", None))

import img_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    room_window = QtGui.QDialog()
    ui = Ui_room_window()
    ui.setupUi(room_window)
    room_window.show()
    sys.exit(app.exec_())

