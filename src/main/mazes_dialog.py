import os
from PyQt5 import QtWidgets, QtGui, uic


class PyMazesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("mazes.ui", self)
        self.ui.drawMazeButton.clicked.connect(self.onDraw)

        self.draw = True

        self.pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        self.pen.setWidth(3)
        self.brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))


    def paintEvent(self, event):
        if self.draw:
            painter = QtGui.QPainter(self)
            painter.setPen(self.pen)
            painter.setBrush(self.brush)
            painter.drawRect(10, 70, 130, 130)

            painter.drawLine(10, 150, 100, 150)


    def onDraw(self):
        index = self.ui.algorithmComboBox.currentIndex()

        self.draw = not self.draw

        self.update()
