from PyQt5 import QtWidgets, QtGui, uic
from src.maze.cell import *
from src.maze.renderer.cellrenderer import *


class PyMazesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = uic.loadUi("mazes.ui", self)
        self.ui.drawMazeButton.clicked.connect(self.onDraw)
        self.ui.widthEdit.setFocus()

        self.draw = True

        self.pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        self.pen.setWidth(2)


    def paintEvent(self, event):
        if self.draw:
            painter = QtGui.QPainter(self)
            painter.setPen(self.pen)

            cellrenderer = CellRenderer(painter, 20, 70)

            for x in range(0, 10):
                cellrenderer.render(Cell(20, x, 0))


    def onDraw(self):
        index = self.ui.algorithmComboBox.currentIndex()

        self.draw = not self.draw

        self.update()
