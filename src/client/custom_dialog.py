# -*- coding: utf-8 -*-
__author__ = 'zhangyang'

from PyQt4 import QtGui, QtCore

class CustomDialog(QtGui.QDialog):
    """
    自定义对话框，本工程所有窗口均继承于此，实现功能如下：
    1.响应了鼠标事件
    2.添加背景图片 self.__texture
    3.添加阴影边框
    4.动画关闭窗口的效果（暂时用不到）
    """
    def __init__(self, parent=None):
        super(CustomDialog, self).__init__(parent)
        self.__mouse_press = False
        self.__texture = ''
        self.__touch_pos = None
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowMinimizeButtonHint |
                            QtCore.Qt.WindowSystemMenuHint |
                            QtCore.Qt.WindowMinMaxButtonsHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:
                #self.setWindowFlags(QtCore.Qt.Window)
                pass
            else:
                self.setWindowFlags(QtCore.Qt.Dialog)
                self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowMinimizeButtonHint |
                            QtCore.Qt.WindowSystemMenuHint |
                            QtCore.Qt.WindowMinMaxButtonsHint)
                self.showNormal()

    @QtCore.pyqtSlot()
    def animateClose(self):
        animation = QtCore.QPropertyAnimation(self, 'windowOpacity', self)
        animation.setDuration(500)
        animation.setStartValue(1)
        animation.setEndValue(0)
        animation.start()
        animation.finished.connect(self.close)

    def setTexture(self, texture):
        self.__texture = texture
        self.update()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if event.y() <= 50:
                self.__mouse_press = True
                self.__touch_pos = event.pos()

    def mouseReleaseEvent(self, event):
        self.__mouse_press = False

    def mouseMoveEvent(self, event):
        if self.__mouse_press:
            self.move(event.globalPos() - self.__touch_pos)

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        global SHADOW_WIDTH
        w = 5

        painter.begin(self)
        self.__drawShadow(painter)
        painter.setPen(QtCore.Qt.NoPen)
        brush = QtGui.QBrush()
        if self.__texture:
            brush.setTexture(QtGui.QPixmap(self.__texture))
            painter.setBrush(brush)
            painter.drawRect(QtCore.QRect(w, w,
                                        self.width()-2*w,
                                        self.height()-2*w))
        painter.end()

    def __drawShadow(self, painter):
        pixmaps = []
        global SHADOW_WIDTH
        pixmaps.append(QtGui.QPixmap(u":/img/shadow/shadow_left.png"))
        pixmaps.append(QtGui.QPixmap(u":/img/shadow/shadow_right.png"))
        pixmaps.append(QtGui.QPixmap(u":/img/shadow/shadow_top.png"))
        pixmaps.append(QtGui.QPixmap(u":/img/shadow/shadow_bottom.png"))
        pixmaps.append(QtGui.QPixmap(u":/img/shadow/shadow_left_top.png"))
        pixmaps.append(QtGui.QPixmap(u":/img/shadow/shadow_right_top.png"))
        pixmaps.append(QtGui.QPixmap(u":/img/shadow/shadow_left_bottom.png"))
        pixmaps.append(QtGui.QPixmap(u":/img/shadow/shadow_right_bottom.png"))

        painter.drawPixmap(0, 0, SHADOW_WIDTH, SHADOW_WIDTH, pixmaps[4])
        painter.drawPixmap(self.width()-SHADOW_WIDTH, 0, SHADOW_WIDTH, SHADOW_WIDTH, pixmaps[5])
        painter.drawPixmap(0,self.height()-SHADOW_WIDTH, SHADOW_WIDTH, SHADOW_WIDTH, pixmaps[6])
        painter.drawPixmap(self.width()-SHADOW_WIDTH,
                           self.height()-SHADOW_WIDTH,
                           SHADOW_WIDTH,
                           SHADOW_WIDTH,
                           pixmaps[7])
        painter.drawPixmap(0, SHADOW_WIDTH,
                           SHADOW_WIDTH,
                           self.height()-2*SHADOW_WIDTH,
                           pixmaps[0].scaled(SHADOW_WIDTH, self.height()-2*SHADOW_WIDTH))
        painter.drawPixmap(self.width()-SHADOW_WIDTH,
                           SHADOW_WIDTH,
                           SHADOW_WIDTH,
                           self.height()-2*SHADOW_WIDTH,
                           pixmaps[1].scaled(SHADOW_WIDTH, self.height()- 2*SHADOW_WIDTH))
        painter.drawPixmap(SHADOW_WIDTH, 0,
                           self.width()-2*SHADOW_WIDTH,
                           SHADOW_WIDTH,
                           pixmaps[2].scaled(self.width()-2*SHADOW_WIDTH, SHADOW_WIDTH))
        painter.drawPixmap(SHADOW_WIDTH,
                           self.height()-SHADOW_WIDTH,
                           self.width()-2*SHADOW_WIDTH,
                           SHADOW_WIDTH,
                           pixmaps[3].scaled(self.width()-2*SHADOW_WIDTH, SHADOW_WIDTH))
SHADOW_WIDTH = 8
