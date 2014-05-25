# -×- coding:utf-8 -*-
__author__ = 'zhangyang'

import time
import gzip

from PyQt4 import QtCore, QtGui
from PyQt4.phonon import *

from ui.Ui_play import Ui_play_window
from custom_dialog import CustomDialog


class PlayWindow(CustomDialog, Ui_play_window):

    send_signal = QtCore.pyqtSignal(dict)
    def __init__(self, num, parent=None):
        super(PlayWindow, self).__init__(parent)

        self.table_num = num
        self.setupUi(self)

        self.chess_list = []
        self.__beautify()
        self.__connectSlots()
        self.__clear_board()

        self.is_white = False
        self.is_playing = False
        self.is_my_turn = 0
        self.my_time_left = 600
        self.his_time_left = 600

        self.time_line = QtCore.QTimeLine(1000, self)
        self.time_line.setFrameRange(1, 21)
        self.time_line.frameChanged.connect(self.test)
        self.time_line.setLoopCount(0)

        self.fd = None
        self.media = Phonon.createPlayer(Phonon.MusicCategory)
        self.media.setTickInterval(62)
        self.media.tick.connect(self.__bad_apple)
        self.media.setCurrentSource(Phonon.MediaSource('badapple/BadApple.mp3'))

    @QtCore.pyqtSlot()
    def __bad_apple(self):
        self.bad_apple.clear()
        for i in range(30):
            try:
                line = self.fd.readline().rstrip()
                self.bad_apple.append(line)
            except:
                return

    #定时器
    def timerEvent(self, event):
        if not self.is_playing: return
        if self.is_my_turn:
            self.my_time_left -= 1
            gm_time = time.gmtime(self.my_time_left)
            self.time_left_1.display(u"%02d:%02d" % (gm_time.tm_min, gm_time.tm_sec))
        else:
            self.his_time_left -=1
            gm_time = time.gmtime(self.his_time_left)
            self.time_left_2.display(u"%02d:%02d" % (gm_time.tm_min, gm_time.tm_sec))

    #帧动画
    @QtCore.pyqtSlot(int)
    def test(self, i):
        self.ani_label.setPixmap(QtGui.QPixmap(u":/img/ani/%02d.png" % i).scaled(self.ani_label.size()))


    ###########################################################
    #游戏状态初始话
    ###########################################################
    @QtCore.pyqtSlot()
    def __clear_board(self):
        for i in self.chess_list:
            i.close()
        self.chess_list = []
        self._board = [([0] * 15) for i in range(15)]

        self.win_label.hide()
        self.ani_label.hide()
        self.lose_btn.hide()
        self.draw_btn.hide()
        self.regret_btn.hide()

    ###########################################################
    #检查有木有赢
    ###########################################################
    def __check_game_over(self, row, column):
        sub = '11111'

        line = ''
        for i in range(15):
            line += str(self._board[row][i])
        if line.find(sub) >= 0:
            return True

        line = ''
        for i in range(15):
            line += str(self._board[i][column])
        if line.find(sub) >= 0:
            return True

        line = ''
        if row > column:
            for i in range(row - column, 15):
                line += str(self._board[i][i - (row - column)])
        else:
            for i in range(column - row, 15):
                line += str(self._board[i - (column - row)][i])
        if line.find(sub) >= 0:
            return True

        line = ''
        for i in range(0, row + column):
            if i >= 0 and i < 15 and row + column - i >= 0 and row + column - i < 15:
                line += str(self._board[i][row + column - i])
        if line.find(sub) >= 0:
            return True
        return False

    ###########################################################
    #美化控件
    ###########################################################
    def __beautify(self):
        self.setTexture(u":/img/skin.png")
        self.min_btn.setAutoDefault(False)
        self.close_btn.setAutoDefault(False)
        self.play_btn.setAutoDefault(False)
        self.regret_btn.setAutoDefault(False)
        self.lose_btn.setAutoDefault(False)
        self.draw_btn.setAutoDefault(False)

        self.name_1.setFont(QtGui.QFont(u"微软雅黑", 9))
        self.name_2.setFont(QtGui.QFont(u"微软雅黑", 9))
        self.win_label.setFont(QtGui.QFont(u"微软雅黑", 40))

        self.lineEdit.setFont(QtGui.QFont(u"微软雅黑", 9))
        self.chat_browser.setFont(QtGui.QFont(u"微软雅黑", 9))

        self.time_left_1.display(u"10:00")
        self.time_left_2.display(u"10:00")
        self.time_left_1.hide()
        self.time_left_2.hide()

        self.white_turn = QtGui.QPixmap(32, 31)
        self.black_turn = QtGui.QPixmap(32, 31)
        self.turn_mask = QtGui.QBitmap(32, 31)
        painter = QtGui.QPainter()
        painter.begin(self.black_turn)
        painter.drawPixmap(0, 0, QtGui.QPixmap(u":/img/2104.bmp"), 0, 0, 32, 31)
        painter.end()

        painter.begin(self.white_turn)
        painter.drawPixmap(0, 0, QtGui.QPixmap(u":/img/2104.bmp"), 32, 0, 32, 31)
        painter.end()

        painter.begin(self.turn_mask)
        painter.drawPixmap(0, 0, QtGui.QPixmap(u":/img/2104.bmp"), 64, 0, 32, 31)
        painter.end()

        self.white_chess = QtGui.QPixmap(33, 33)
        self.black_chess = QtGui.QPixmap(33, 33)
        self.chess_mask = QtGui.QBitmap(33, 33)
        painter = QtGui.QPainter()
        painter.begin(self.black_chess)
        painter.drawPixmap(0, 0, QtGui.QPixmap(u":/img/2096.bmp"), 0, 0, 33, 33)
        painter.end()

        painter.begin(self.white_chess)
        painter.drawPixmap(0, 0, QtGui.QPixmap(u":/img/2096.bmp"), 33, 0, 33, 33)
        painter.end()

        painter.begin(self.chess_mask)
        painter.drawPixmap(0, 0, QtGui.QPixmap(u":/img/2096.bmp"), 66, 0, 33, 33)
        painter.end()

        self.pic_1.setPixmap(QtGui.QPixmap(u":img/01299.png").scaled(self.pic_1.size()))
        self.pic_2.setPixmap(QtGui.QPixmap(u":img/01299.png").scaled(self.pic_2.size()))
        self.pic_2.hide()



    ###########################################################
    #连接信号与槽
    ###########################################################
    def __connectSlots(self):
        self.min_btn.setAutoDefault(False)
        self.close_btn.setAutoDefault(False)

        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.leave_game)
        self.play_btn.clicked.connect(self.play_btn_clicked)
        self.regret_btn.clicked.connect(self.regret_btn_clicked)
        self.lose_btn.clicked.connect(self.lose_btn_clicked)

        self.send_btn.clicked.connect(self.__send_message)
        self.lineEdit.returnPressed.connect(self.__send_message)


    ###########################################################
    #根据新x，y的值计算落在棋盘的哪个点上，返回第几行第几列
    ###########################################################
    def chessPos(self, x, y):
        _x = abs(x - 218)
        _y = abs(y - 122)
        column = _x / 35
        if _x % 35 >= 25:
            column += 1
        row = _y / 35
        if _y % 35 >= 25:
            row += 1
        return row, column

    ###########################################################
    #在相应的位置放置一个棋子，如果可以的话
    ###########################################################
    def clickInBoard(self, x, y):
        if not self.is_playing:
            return
        if not self.is_my_turn:
            return

        row, column = self.chessPos(x, y)
        _x = column * 35 + 218 - 16
        _y = row * 35 + 122 - 16

        if self._board[row][column]:
            return

        label = QtGui.QLabel(self.board)
        if self.is_white:
            label.setPixmap(self.white_chess)
            label.setMask(self.chess_mask)
        else:
            label.setPixmap(self.black_chess)
            label.setMask(self.chess_mask)
        label.setFixedSize(33, 33)
        label.move(_x, _y)
        label.show()
        self.chess_list.append(label)
        self.is_my_turn = 0
        self._board[row][column] = 1

        msg = {
            'sid': 2001,
            'cid': 1004,
            'table': self.table_num,
            'pos': [row, column],
            'win': self.__check_game_over(row, column)
        }

        self.send_signal.emit(msg)

        self.time_left_1.display(u"10:00")
        self.his_time_left = 600
        self.regret_btn.show()

        if self.__check_game_over(row, column):
            self.set_win(True)

    ###########################################################
    #游戏开始，认输，和局按钮显示
    ###########################################################
    def set_game_started(self):
        self.is_playing = 1
        self.set_opponent_prepared()
        if self.is_white:
            self.is_my_turn = 1
        self.timer_id = self.startTimer(1000)
        self.draw_btn.show()
        self.lose_btn.show()

    ###########################################################
    #对手准备
    ###########################################################
    def set_opponent_prepared(self):
        if self.is_white:
            self.his_chess.setPixmap(self.black_turn)
        else:
            self.his_chess.setPixmap(self.white_turn)
        self.his_chess.setMask(self.turn_mask)
        self.his_chess.show()

    ###########################################################
    #对手下棋的位置
    ###########################################################
    def set_opponent_pos(self, row, column):
        self._board[row][column] = 2
        _x = column * 35 + 218 - 16
        _y = row * 35 + 122 - 16

        label = QtGui.QLabel(self.board)
        if self.is_white:
            label.setPixmap(self.black_chess)
            label.setMask(self.chess_mask)
        else:
            label.setPixmap(self.white_chess)
            label.setMask(self.chess_mask)
        label.setFixedSize(33, 33)
        label.move(_x, _y)
        label.show()
        self.chess_list.append(label)
        self.is_my_turn = 1

        self.my_time_left = 600
        self.time_left_2.display(u"10:00")

        self.regret_btn.hide()

    ###########################################################
    #输了还是赢了
    ###########################################################
    def set_win(self, win):
        self.killTimer(self.timer_id)
        if win:
            self.win_label.setText(u"Yeah!!赢了!")
        else:
            self.win_label.setText(u"Yeah!!输了!")

        #self.time_line.finished.connect(self.__clear_board)
        self.win_label.show()
        self.ani_label.show()
        self.time_line.start()
        self.is_playing = False
        self.is_my_turn = 0

        self.play_btn.show()
        self.regret_btn.hide()
        self.draw_btn.hide()
        self.lose_btn.hide()

        self.his_chess.hide()
        self.my_chess.hide()

    ###########################################################
    #离开游戏
    ###########################################################
    @QtCore.pyqtSlot()
    def leave_game(self):
        # if self.is_playing:
        #     print 'is playing, can not quit'
        #     return
        self.media.stop()
        if self.fd:
            self.fd.close()
        msg = {
            'sid': 2001,
            'cid': 1002,
            'table': self.table_num
        }
        self.send_signal.emit(msg)
        self.close()

    ###########################################################
    #点击开始游戏
    ###########################################################
    @QtCore.pyqtSlot()
    def play_btn_clicked(self):
        if self.fd:
            self.fd.seek(0)
        else:
            self.fd = gzip.open('badapple/BadApple.dat', 'rb')
        self.bad_apple.clear()
        self.media.stop()
        self.media.play()

        if self.time_line:
            self.time_line.stop()
        self.__clear_board()
        self.play_btn.hide()
        if self.is_white:
            self.my_chess.setPixmap(self.white_turn)
        else:
            self.my_chess.setPixmap(self.black_turn)
        self.my_chess.setMask(self.turn_mask)
        self.my_chess.show()

        msg = {
            'sid': 2001,
            'cid': 1003,
            'table': self.table_num
        }
        self.send_signal.emit(msg)

    ###########################################################
    #点击认输
    ###########################################################
    @QtCore.pyqtSlot()
    def __send_message(self):
        txt = self.lineEdit.text()
        if txt == '':
            return

        self.lineEdit.clear()
        self.chat_browser.append(u"<font color='red'>我 -  说：</>")
        self.chat_browser.append(u"    " + txt)
        msg = {
            'sid': 2002,
            'cid': 1002,
            'table': self.table_num,
            'content': unicode(txt.toUtf8(), 'utf-8', 'ignore')
        }
        self.send_signal.emit(msg)

    ###########################################################
    #点击认输
    ###########################################################
    @QtCore.pyqtSlot()
    def lose_btn_clicked(self):
        pass

    ###########################################################
    #点击悔棋
    ###########################################################
    @QtCore.pyqtSlot()
    def regret_btn_clicked(self):
        msg = {
            'sid': 2001,
            'cid': 1005,
            'table': self.table_num,
            'type': 0
        }
        self.regret_label = QtGui.QLabel(self.board)
        self.regret_label.setStyleSheet(u"background-image:url(:img/sta_tip.bmp); padding-left:60px;")
        self.regret_label.resize(250, 47)
        self.regret_label.move(342, 347)
        self.regret_label.setText(u"等待对手回应")
        self.regret_label.show()
        self.send_signal.emit(msg)
        self.regret_btn.hide()

    def un_do(self):
        last_step = self.chess_list.pop()
        x = last_step.x()
        y = last_step.y()
        column = (x + 16 - 218) / 35
        row = (y + 16 - 122) / 35
        self._board[row][column] = 0
        last_step.close()
        self.is_my_turn = 1 - self.is_my_turn

    ###########################################################
    #重写鼠标点击事件，判断是否点击在棋盘上
    ###########################################################
    def mousePressEvent(self, event):
        super(PlayWindow, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            if event.y() > 50:
                x = event.x()
                y = event.y()
                b_x = self.board.x()
                b_y = self.board.y()
                if x >= b_x + 210 and x <= b_x + 720 and y >= b_y + 115 and y < b_y + 625:
                    self.clickInBoard(x - b_x, y - b_y)