# -*- coding: utf-8 -*-
__author__ = 'zhangyang'

from PyQt4 import QtGui, QtCore

class EasyAnimation(QtCore.QObject):
    left_right = 1
    top_bottom = 2
    def __init__(self, parent=None):
        super(EasyAnimation, self).__init__(parent)
        self.duration_1 = 1000
        self.duration_2 = 1000
        self.direction = 1
        self.closing = True

    animationStarted = QtCore.pyqtSignal()
    animationFinished = QtCore.pyqtSignal()

    def setClosing(self, t):
        self.closing = t

    def setDuration(self, d1, d2):
        self.duration_1 = d1
        self.duration_2 = d2

    def setDirection(self, d):
        self.direction = d

    def setWidgets(self, first, second):
        self.first = first
        self.second = second


    # def prepareAnimation(self):
    #     self.first_pix = QtGui.QPixmap(self.first.width()-10, self.first.height()-10)
    #     rect = QtCore.QRect(5, 5, self.first.width()-10, self.first.height()-10)
    #     self.first.render(self.first_pix, QtCore.QPoint(0,0), QtGui.QRegion(rect))
    #
    #     self.second_pix = QtGui.QPixmap(self.second.width()-10, self.second.height()-10)
    #     rect = QtCore.QRect(5, 5, self.second.width()-10, self.second.height()-10)
    #     self.second.render(self.second_pix, QtCore.QPoint(0,0), QtGui.QRegion(rect))
    #
    #     self.animationStarted.emit()
    #     self.starAnimation()

    def startAnimation(self):
        # self.label = QtGui.QLabel()
        # self.label.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.label.setPixmap(self.first_pix)
        # self.label.resize(self.first_pix.size())
        # self.label.setScaledContents(True)
        # self.label.show()

        if self.direction == 1:
            point = QtCore.QPoint(-1200, self.first.pos().y())
        else:
            point = QtCore.QPoint(self.first.pos().x(), 1200)


        animation = QtCore.QPropertyAnimation(self.first, 'pos', self)
        animation.setDuration(self.duration_1)
        animation.setStartValue(self.first.pos())
        animation.setEndValue(point)
        animation.finished.connect(self.__anotherAnimation)
        animation.start()

    @QtCore.pyqtSlot()
    def __anotherAnimation(self):
        self.second.show()
        if self.closing:
            self.first.close()
        else:
            self.first.showMinimized()
            self.first.move(400, 200)

        if self.direction == 1:
            self.second.move(-1200, 100)
        else:
            self.second.move(100, -1200)

        animation = QtCore.QPropertyAnimation(self.second, 'pos', self)
        animation.setDuration(self.duration_2)

        animation.setStartValue(self.second.pos())
        animation.setEndValue(QtCore.QPoint(100, 100))
        animation.setEasingCurve(QtCore.QEasingCurve.OutBack)
        animation.finished.connect(self.animationFinished)
        animation.start()


