from PyQt5 import QtWidgets, QtGui, uic
from ..maze.maze import Cell, Maze
from ..maze.renderer.mazerenderer import MazeRenderer


class PyMazesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = uic.loadUi("mazes.ui", self)
        self.ui.drawMazeButton.clicked.connect(self.onDraw)
        self.ui.widthEdit.setFocus()

        self.draw = False

        self.pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        self.pen.setWidth(2)

        self.baseX = 20
        self.baseY = 70

    def paintEvent(self, event):
        if self.draw:
            mazerenderer = MazeRenderer(self.get_painter(), self.baseX, self.baseY)
            mazerenderer.render(self.maze);

    def onDraw(self):
        width = int(self.ui.widthEdit.text())
        height = int(self.ui.heightEdit.text())

        self.maze = Maze(20, width, height)

        index = self.ui.algorithmComboBox.currentIndex()

        self.draw = True

        self.update()

    def get_painter(self):
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)

        return painter
