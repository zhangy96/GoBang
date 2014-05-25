# -*- coding:utf-8 -*-
__author__ = 'gzs2473'

from PyQt4 import QtCore
from PyQt4 import QtGui

from ui.Ui_room import Ui_room_window
from table_widget import TableWidget
from play_window import PlayWindow
from custom_dialog import CustomDialog


class RoomWindow(CustomDialog, Ui_room_window):
    send_signal = QtCore.pyqtSignal(dict)
    enter_table_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(RoomWindow, self).__init__(parent)

        self.table_num = -1  #记录当前用户在哪个桌子，-1表示不在任何桌子
        #记录哪个桌子已经有人
        self.tables = [([0] * 2) for i in range(16)]

        self.setupUi(self)
        self.__beautify()
        self.__connect_slots()

    ###########################################################
    #美化控件
    ###########################################################
    def __beautify(self):
        self.setTexture(u":/img/skin.png")
        self.min_btn.setAutoDefault(False)
        self.close_btn.setAutoDefault(False)
        self.title_label.setFont(QtGui.QFont(u"微软雅黑", 9))
        self.title_label.setText(u"  五子棋 made by 9527")
        self.count_label.setFont(QtGui.QFont(u"微软雅黑", 9))
        self.textBrowser.setFont(QtGui.QFont(u"微软雅黑", 9))
        self.lineEdit.setFont(QtGui.QFont(u"微软雅黑", 9))
        self.score_label.setFont(QtGui.QFont(u"微软雅黑", 9))
        self.record_label.setFont(QtGui.QFont(u"微软雅黑", 9))
        self.name_label.setFont(QtGui.QFont(u"微软雅黑", 11))
        self.players_btn.setFont(QtGui.QFont(u"微软雅黑",8))
        self.rank_btn.setFont(QtGui.QFont(u"微软雅黑",8))
        self.players_btn.setText(u"玩家列表")
        self.rank_btn.setText(u"排行榜")
        self.rank_4.setFont(QtGui.QFont(u"华文行楷", 16))
        self.rank_5.setFont(QtGui.QFont(u"华文行楷", 16))

        self.rank_table.horizontalHeader().resizeSection(0, 180)
        self.rank_table.setFont(QtGui.QFont(u"微软雅黑", 10))
        self.stackedWidget.setCurrentIndex(0)

    ###########################################################
    #连接信号与槽
    ###########################################################
    def __connect_slots(self):
        self.lineEdit.returnPressed.connect(self.__send_message)
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.quit)
        self.send_btn.clicked.connect(self.__send_message)

        self.mapper = QtCore.QSignalMapper()
        self.__init_tables(16)
        self.mapper.mapped.connect(self.__enter_table)

        self.players_btn.clicked.connect(self.__show_players)
        self.rank_btn.clicked.connect(self.__show_rank)

    def set_rank_list(self, items):
        if not items: return
        for i in range(5):
            self.rank_table.setItem(i, 0, QtGui.QTableWidgetItem(items[i][0]))
            self.rank_table.setItem(i, 1, QtGui.QTableWidgetItem(u"积分：%d" % items[i][1]))

    @QtCore.pyqtSlot()
    def __show_players(self):
        self.stackedWidget.setCurrentIndex(0)

    @QtCore.pyqtSlot()
    def __show_rank(self):
        self.stackedWidget.setCurrentIndex(1)
    ###########################################################
    #添加游戏大厅里的桌子
    #简单起见，只添加16个桌子
    ###########################################################
    def __init_tables(self, num):
        for i in xrange(num):
            table_widget = TableWidget()
            table_widget.setObjectName(u"table%d" % i)
            table_widget.setStyleSheet(u"QWidget#table%d{background-image: url(:/img/tablen.bmp);}" % i)
            self.gridLayout.addWidget(table_widget, i / 4, i % 4, 1, 1)
            table_widget.left_btn.clicked.connect(self.mapper.map)
            table_widget.right_btn.clicked.connect(self.mapper.map)
            self.mapper.setMapping(table_widget.left_btn, i * 100 + 0)
            self.mapper.setMapping(table_widget.right_btn, i * 100 + 1)

    ###########################################################
    #进入赌桌
    ###########################################################
    @QtCore.pyqtSlot(int)
    def __enter_table(self, num):
        #如果这个位置已经有人了
        if self.tables[num / 100][num % 100]:
            return
        if self.table_num >= 0:
            return

        self.table_num = num
        self.tables[num / 100][num % 100] = 1

        msg = {
            'sid': 2001,
            'cid': 1001,
            'table': num
        }

        self.play_window = PlayWindow(num)
        self.play_window.close_btn.clicked.connect(self.__leave_table)
        if self.tables[num / 100][1 - num % 100]:
            self.play_window.is_white = 0
        else:
            self.play_window.is_white = 1

        table_widget = self.findChild(TableWidget, u"table%d" % (num / 100))
        if num % 100:
            table_widget.right_btn.setStyleSheet(u"background-image:url(:/img/17-1.png);background-color:transparent;")
        else:
            table_widget.left_btn.setStyleSheet(u"background-image:url(:/img/17-1.png);background-color:transparent;")
        self.send_signal.emit(msg)
        self.enter_table_signal.emit(num)

    ###########################################################
    #离开赌桌
    ###########################################################
    @QtCore.pyqtSlot()
    def __leave_table(self):
        table_widget = self.findChild(TableWidget, u"table%d" % (self.table_num / 100))
        if self.table_num % 100:
            table_widget.right_btn.setStyleSheet(u"background-color:transparent;")
        else:
            table_widget.left_btn.setStyleSheet(u"background-color:transparent;")

        self.tables[self.table_num / 100][self.table_num % 100] = 0
        self.table_num = -1

    ###########################################################
    #游戏大厅的聊天室功能
    ###########################################################
    @QtCore.pyqtSlot()
    def __send_message(self):
        txt = self.lineEdit.text()
        if txt == '':
            return

        self.lineEdit.clear()
        self.textBrowser.append(u"<font color='red'>我 -  说：</>")
        self.textBrowser.append(u"    " + txt)
        msg = {
            'sid': 2002,
            'cid': 1001,
            'content': unicode(txt.toUtf8(), 'utf-8', 'ignore')
        }
        self.send_signal.emit(msg)


    ###########################################################
    #退出大厅的时候，通知服务器离开
    ###########################################################
    @QtCore.pyqtSlot()
    def quit(self):
        msg = {
            'sid': 2000,
            'cid': 1002,
        }
        self.send_signal.emit(msg)
        self.close()