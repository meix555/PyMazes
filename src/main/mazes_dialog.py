from PyQt5 import QtWidgets, QtGui, uic
from ..maze.maze import Cell, Maze
from ..maze.renderer.mazerenderer import MazeRenderer
from ..maze.factory.mazefactory_binarytree import MazeFactoryBinaryTree
from ..maze.factory.mazefactory_sidewinder import MazeFactorySidewinder
from ..maze.factory.mazefactory_aldousbroder import MazeFactoryAldousBroder
from ..maze.factory.mazefactory_wilson import MazeFactoryWilson


class PyMazesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = uic.loadUi("mazes.ui", self)
        self.ui.drawMazeButton.clicked.connect(self.onDraw)
        self.ui.widthEdit.setFocus()

        self.draw = False

        self.pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        self.pen.setWidth(2)

        self.base_x = 20
        self.base_y = 70

        self.factories = self.create_factorylist()


    def paintEvent(self, event):
        if self.draw:
            mazerenderer = MazeRenderer(self.get_painter(), self.base_x, self.base_y)
            mazerenderer.render(self.maze);


    def onDraw(self):
        width = int(self.ui.widthEdit.text())
        height = int(self.ui.heightEdit.text())

        index = self.ui.algorithmComboBox.currentIndex()
        mazefactory = self.factories[index]

        self.maze = mazefactory.create_maze(20, width, height)

        self.draw = True

        self.update()


    def get_painter(self):
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)

        return painter


    def create_factorylist(self):
        factories = [MazeFactoryBinaryTree(), MazeFactorySidewinder(), MazeFactoryAldousBroder(),
                     MazeFactoryWilson()]

        return factories
