# -*- coding: utf-8 -*-
__author__ = 'gzs2473'

import socket
import json
import sys
import logging

from PyQt4 import QtGui
from PyQt4 import QtCore

from client.login_window import LoginWindow
from client.room_window import RoomWindow
from client.table_widget import TableWidget
from client.custom_animation import EasyAnimation


class CMD(object):
    LOG_IN_OUT = (1000, 1001, 1002)
    CHAT = (1003, 1004)
    PLAY = (1005, 10051, 1006, 1007, 1008, 1009, 1010)

class Client(QtCore.QObject):
    def __init__(self, parent=None):
        super(Client, self).__init__(parent)
        self.login_window = LoginWindow()
        self.login_window.login_signal.connect(self.login_btn_clicked)
        self.login_window.show()
        self.room_window = None
        self.play_window = None

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timer_id = self.startTimer(100)

    def timerEvent(self, event):
        try:
            msg = self.sock.recv(1024)
            if not msg:
                print 'Remote server shutdown'
                return
            msg = json.loads(msg)
            if msg['cid'] in CMD.LOG_IN_OUT:
                self.__handle_login_out(msg)
            elif msg['cid'] in CMD.PLAY:
                self.__handle_play(msg)
            elif msg['cid'] in CMD.CHAT:
                self.__handle_chat(msg)
        except socket.error:
            return

    @QtCore.pyqtSlot(str, int, str)
    def login_btn_clicked(self, ip, port, name):
        try:
            self.sock.connect((ip, port))
        except socket.error as e:
            print e
            return
        else:
            msg = {
                'sid': 2000,
                'cid': 1001,
                'name': unicode(name.toUtf8(), 'utf-8', 'ignore')
            }
            self.sock.setblocking(False)
            self.send_to_server(msg)
            self.room_window = RoomWindow()
            self.login_window.close()
            self.room_window.show()
            self.room_window.send_signal.connect(self.send_to_server)
            self.room_window.enter_table_signal.connect(self.enter_table)

    @QtCore.pyqtSlot(int)
    def enter_table(self, num):
        self.play_window = self.room_window.play_window
        self.play_window.send_signal.connect(self.send_to_server)

    @QtCore.pyqtSlot(dict)
    def send_to_server(self, msg):
        try:
            self.sock.send(json.dumps(msg))
        except socket.error as e:
            print e

    ###########################################################
    #处理服务端发来的指令：用户加入离开
    #1000：从服务器获得的初始化数据
    #1001：有新用户加入
    #1002：有用户离开
    ###########################################################
    def __handle_login_out(self, msg):
        total_players = msg['total_players']
        self.room_window.count_label.setText(u'当前在线人数：%d人' % total_players)
        if msg['cid'] == 1000:
            players = msg['player_list']
            tables = msg['table_list']
            self.nick_name = players[0]
            for player in players:
                item = QtGui.QListWidgetItem(QtGui.QIcon(u":/img/17-1.png"), player)
                self.room_window.player_list.addItem(item)

            for table in tables:
                self.room_window.tables[table / 100][table % 100] = 1
                table_widget = self.room_window.findChild(TableWidget, u"table%d" % (table / 100))
                if table % 100:
                    table_widget.right_btn.setStyleSheet(
                        u"border-image:url(:/img/17-1.png);background-color:transparent;")
                else:
                    table_widget.left_btn.setStyleSheet(
                        u"border-image:url(:/img/17-1.png);background-color:transparent;")
            user_info = msg['user_info']
            if user_info:
                self.room_window.name_label.setText(user_info[0]+', welcome back')
                if user_info[1] == 0: ratio = 0
                else: ratio = float(user_info[1])/(user_info[1]+user_info[2]+user_info[3])
                record_str = u"胜：%d\t负：%d\t平：%d\t胜率：%.2f%%" % (user_info[1],
                                                          user_info[2],
                                                          user_info[3],
                                                          ratio*100)
                self.room_window.record_label.setText(record_str)
                self.room_window.score_label.setText(u"积分：%s" % user_info[4])
            else:
                self.room_window.name_label.setText('Welcome, '+self.nick_name)
                self.room_window.record_label.setText(u"胜：0\t负：0\t平：0\t胜率：0%")
                self.room_window.score_label.setText(u"积分：0")
            self.room_window.set_rank_list(msg['rank'])

        elif msg['cid'] == 1001:
            player = msg['name']
            item = QtGui.QListWidgetItem(QtGui.QIcon(u":/img/17-1.png"), player)
            self.room_window.player_list.addItem(item)

        elif msg['cid'] == 1002:
            pass

    ###########################################################
    #处理聊天
    #1003：房间聊天
    #1004：桌子聊天
    ###########################################################
    def __handle_chat(self, msg):
        if msg['cid'] == 1003:
            who = msg['who']
            content = msg['content']
            self.room_window.textBrowser.append(u"<font color='blue'>%s -  说：</>" % who)
            self.room_window.textBrowser.append('    ' + content)

        elif msg['cid'] == 1004:
            who = msg['who']
            content = msg['content']
            if self.play_window:
                self.play_window.chat_browser.append(u"<font color='blue'>%s -  说：</>" % who)
                self.play_window.chat_browser.append('    ' + content)


    def __handle_play(self, msg):
        #有人进入了桌子
        if msg['cid'] == 1005:
            table = msg['table']
            self.room_window.tables[table / 100][table % 100] = 1
            table_widget = self.room_window.findChild(TableWidget, u"table%d" % (table / 100))
            if table % 100:
                table_widget.right_btn.setStyleSheet(u"border-image:url(:/img/17-1.png);background-color:transparent;")
            else:
                table_widget.left_btn.setStyleSheet(u"border-image:url(:/img/17-1.png);background-color:transparent;")

            if self.room_window.table_num / 100 == table / 100:
                if self.play_window:
                    self.play_window.pic_2.show()
                    self.play_window.name_2.setText(msg['name'])
                    self.play_window.time_left_2.show()

        #当进入桌子的时候，服务器返回10051指令，包含桌子信息
        elif msg['cid'] == 10051:
            self.ani = EasyAnimation()
            self.ani.setWidgets(self.room_window, self.play_window)
            self.ani.setDirection(EasyAnimation.top_bottom)
            self.ani.setDuration(400, 700)
            self.ani.setClosing(False)
            self.ani.startAnimation()
            self.play_window.pic_1.show()
            self.play_window.name_1.setText(self.nick_name)
            self.play_window.time_left_1.show()
            if msg['has_opponent']:
                self.play_window.pic_2.show()
                self.play_window.name_2.setText(msg['name'])
                self.play_window.time_left_2.show()
                if msg['state'] == 3:
                    self.play_window.set_opponent_prepared()

        #有人离开了桌子
        elif msg['cid'] == 1006:
            table = msg['table']
            self.room_window.tables[table / 100][table % 100] = 0
            table_widget = self.room_window.findChild(TableWidget, u"table%d" % (table / 100))
            if table % 100:
                table_widget.right_btn.setStyleSheet(u"background-color:transparent;")
            else:
                table_widget.left_btn.setStyleSheet(u"background-color:transparent;")

            if self.room_window.table_num / 100 == table / 100:
                self.play_window.pic_2.hide()
                self.play_window.name_2.setText(u"")
                self.play_window.time_left_2.hide()
                self.play_window.is_white = 1

        #开始游戏
        elif msg['cid'] == 1007:
            self.play_window.set_game_started()

        #对手已经准备
        elif msg['cid'] == 1008:
            self.play_window.set_opponent_prepared()

        #下棋的位置
        elif msg['cid'] == 1009:
            x = msg['pos'][0]
            y = msg['pos'][1]
            self.play_window.set_opponent_pos(x, y)
            if msg['win']:
                self.play_window.set_win(False)

        elif msg['cid'] == 1010:
            ask_reply = msg['type']
            if ask_reply == 0:
                _msg = {
                    'sid': 2001,
                    'cid': 1005,
                    'table': self.room_window.table_num,
                    'type': 1,
                    'agree': 1
                }
                result = QtGui.QMessageBox.information(self.play_window,
                                                       u"请求",
                                                       u"对手请求悔棋",
                                                       u"同意",
                                                       u"不同意")
                if result == 1:
                    _msg['agree'] = 0
                else:
                    self.play_window.un_do()

                self.send_to_server(_msg)
            else:
                if msg['agree']:
                    self.play_window.regret_label.setText(u"对手同意了")
                    self.play_window.un_do()
                else:
                    self.play_window.regret_label.setText(u"对手拒绝了")
                self.ani = QtCore.QPropertyAnimation(self.play_window.regret_label, 'windowOpacity', self)
                self.ani.setStartValue(1)
                self.ani.setEndValue(0)
                self.ani.setDuration(1000)
                self.ani.start()
                self.ani.finished.connect(self.play_window.regret_label.close)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    client = Client()
    sys.exit(app.exec_())
    client.killTimer(client.timer_id)
