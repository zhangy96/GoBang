# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PyCharm_Project\GoBang\src\client\ui\play.ui'
#
# Created: Fri May 23 18:12:04 2014
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

class Ui_play_window(object):
    def setupUi(self, play_window):
        play_window.setObjectName(_fromUtf8("play_window"))
        play_window.resize(1264, 775)
        play_window.setStyleSheet(_fromUtf8("QScrollBar{\n"
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
        self.verticalLayout = QtGui.QVBoxLayout(play_window)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.min_btn = QtGui.QPushButton(play_window)
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
        self.close_btn = QtGui.QPushButton(play_window)
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
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.board = QtGui.QWidget(play_window)
        self.board.setMinimumSize(QtCore.QSize(739, 735))
        self.board.setMaximumSize(QtCore.QSize(739, 735))
        self.board.setStyleSheet(_fromUtf8("QWidget#board{\n"
"background-image: url(:/img/2063.bmp);\n"
"}\n"
""))
        self.board.setObjectName(_fromUtf8("board"))
        self.player_top = QtGui.QWidget(self.board)
        self.player_top.setGeometry(QtCore.QRect(4, 101, 191, 262))
        self.player_top.setMinimumSize(QtCore.QSize(191, 262))
        self.player_top.setStyleSheet(_fromUtf8("QWidget#player_top{background-image: url(:/img/2083.bmp);\n"
"}"))
        self.player_top.setObjectName(_fromUtf8("player_top"))
        self.my_chess = QtGui.QLabel(self.player_top)
        self.my_chess.setGeometry(QtCore.QRect(15, 190, 32, 31))
        self.my_chess.setText(_fromUtf8(""))
        self.my_chess.setObjectName(_fromUtf8("my_chess"))
        self.pic_1 = QtGui.QLabel(self.player_top)
        self.pic_1.setGeometry(QtCore.QRect(16, 0, 160, 160))
        self.pic_1.setText(_fromUtf8(""))
        self.pic_1.setObjectName(_fromUtf8("pic_1"))
        self.name_1 = QtGui.QLabel(self.player_top)
        self.name_1.setGeometry(QtCore.QRect(67, 170, 100, 20))
        self.name_1.setStyleSheet(_fromUtf8("color:white;"))
        self.name_1.setText(_fromUtf8(""))
        self.name_1.setObjectName(_fromUtf8("name_1"))
        self.time_left_1 = QtGui.QLCDNumber(self.player_top)
        self.time_left_1.setGeometry(QtCore.QRect(65, 200, 111, 41))
        self.time_left_1.setFrameShape(QtGui.QFrame.Panel)
        self.time_left_1.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.time_left_1.setProperty("intValue", 0)
        self.time_left_1.setObjectName(_fromUtf8("time_left_1"))
        self.player_bottom = QtGui.QWidget(self.board)
        self.player_bottom.setGeometry(QtCore.QRect(4, 377, 191, 262))
        self.player_bottom.setMinimumSize(QtCore.QSize(191, 262))
        self.player_bottom.setStyleSheet(_fromUtf8("QWidget#player_bottom{background-image: url(:/img/2124.bmp);\n"
"}"))
        self.player_bottom.setObjectName(_fromUtf8("player_bottom"))
        self.his_chess = QtGui.QLabel(self.player_bottom)
        self.his_chess.setGeometry(QtCore.QRect(14, 40, 32, 31))
        self.his_chess.setText(_fromUtf8(""))
        self.his_chess.setObjectName(_fromUtf8("his_chess"))
        self.pic_2 = QtGui.QLabel(self.player_bottom)
        self.pic_2.setGeometry(QtCore.QRect(15, 99, 160, 160))
        self.pic_2.setText(_fromUtf8(""))
        self.pic_2.setObjectName(_fromUtf8("pic_2"))
        self.name_2 = QtGui.QLabel(self.player_bottom)
        self.name_2.setGeometry(QtCore.QRect(67, 15, 100, 20))
        self.name_2.setStyleSheet(_fromUtf8("color:white;"))
        self.name_2.setText(_fromUtf8(""))
        self.name_2.setObjectName(_fromUtf8("name_2"))
        self.time_left_2 = QtGui.QLCDNumber(self.player_bottom)
        self.time_left_2.setGeometry(QtCore.QRect(64, 46, 111, 41))
        self.time_left_2.setFrameShape(QtGui.QFrame.Panel)
        self.time_left_2.setFrameShadow(QtGui.QFrame.Raised)
        self.time_left_2.setSegmentStyle(QtGui.QLCDNumber.Outline)
        self.time_left_2.setProperty("intValue", 0)
        self.time_left_2.setObjectName(_fromUtf8("time_left_2"))
        self.play_btn = QtGui.QPushButton(self.board)
        self.play_btn.setGeometry(QtCore.QRect(442, 677, 56, 24))
        self.play_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2072.bmp) 0 112 0 0;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2072.bmp) 0 56 0 56;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2072.bmp) 0 0 0 112;\n"
"}"))
        self.play_btn.setText(_fromUtf8(""))
        self.play_btn.setObjectName(_fromUtf8("play_btn"))
        self.regret_btn = QtGui.QPushButton(self.board)
        self.regret_btn.setGeometry(QtCore.QRect(211, 658, 43, 21))
        self.regret_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2068.bmp) 0 86 0 0;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2068.bmp) 0 43 0 43;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2068.bmp) 0 0 0 86;\n"
"}"))
        self.regret_btn.setText(_fromUtf8(""))
        self.regret_btn.setObjectName(_fromUtf8("regret_btn"))
        self.lose_btn = QtGui.QPushButton(self.board)
        self.lose_btn.setGeometry(QtCore.QRect(516, 672, 46, 24))
        self.lose_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2070.bmp) 0 92 0 0;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2070.bmp) 0 46 0 46;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2070.bmp) 0 0 0 92;\n"
"}"))
        self.lose_btn.setText(_fromUtf8(""))
        self.lose_btn.setObjectName(_fromUtf8("lose_btn"))
        self.ani_label = QtGui.QLabel(self.board)
        self.ani_label.setGeometry(QtCore.QRect(240, 150, 450, 450))
        self.ani_label.setStyleSheet(_fromUtf8("color:red;"))
        self.ani_label.setText(_fromUtf8(""))
        self.ani_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ani_label.setObjectName(_fromUtf8("ani_label"))
        self.draw_btn = QtGui.QPushButton(self.board)
        self.draw_btn.setGeometry(QtCore.QRect(372, 673, 45, 24))
        self.draw_btn.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2067.bmp) 0 90 0 0;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2067.bmp) 0 45 0 45;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:transparent;\n"
"border-image:url(:/img/2067.bmp) 0 0 0 90;\n"
"}"))
        self.draw_btn.setText(_fromUtf8(""))
        self.draw_btn.setObjectName(_fromUtf8("draw_btn"))
        self.win_label = QtGui.QLabel(self.board)
        self.win_label.setGeometry(QtCore.QRect(300, 150, 331, 91))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.win_label.setFont(font)
        self.win_label.setStyleSheet(_fromUtf8("color:red"))
        self.win_label.setText(_fromUtf8(""))
        self.win_label.setAlignment(QtCore.Qt.AlignCenter)
        self.win_label.setObjectName(_fromUtf8("win_label"))
        self.horizontalLayout_2.addWidget(self.board)
        self.right_widget = QtGui.QWidget(play_window)
        self.right_widget.setStyleSheet(_fromUtf8(""))
        self.right_widget.setObjectName(_fromUtf8("right_widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.right_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.bad_apple = QtGui.QTextBrowser(self.right_widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(8)
        self.bad_apple.setFont(font)
        self.bad_apple.setStyleSheet(_fromUtf8("border:0px;background-color:rgba(255,255,255,180);"))
        self.bad_apple.setLineWrapMode(QtGui.QTextEdit.FixedColumnWidth)
        self.bad_apple.setLineWrapColumnOrWidth(80)
        self.bad_apple.setObjectName(_fromUtf8("bad_apple"))
        self.verticalLayout_2.addWidget(self.bad_apple)
        self.line = QtGui.QFrame(self.right_widget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.chat_browser = QtGui.QTextBrowser(self.right_widget)
        self.chat_browser.setMinimumSize(QtCore.QSize(0, 270))
        self.chat_browser.setStyleSheet(_fromUtf8("border:0px;"))
        self.chat_browser.setObjectName(_fromUtf8("chat_browser"))
        self.verticalLayout_2.addWidget(self.chat_browser)
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
        self.verticalLayout_2.addWidget(self.chat_widget)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.addWidget(self.right_widget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(play_window)
        QtCore.QMetaObject.connectSlotsByName(play_window)

    def retranslateUi(self, play_window):
        play_window.setWindowTitle(_translate("play_window", "Dialog", None))
        self.bad_apple.setHtml(_translate("play_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:4pt;\"><br /></p></body></html>", None))

import img_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    play_window = QtGui.QDialog()
    ui = Ui_play_window()
    ui.setupUi(play_window)
    play_window.show()
    sys.exit(app.exec_())

