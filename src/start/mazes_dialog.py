from PyQt5 import QtWidgets, QtGui, uic

from src.maze.factory.maze_factory_empty_maze import MazeFactoryEmptyMaze
from src.maze.factory.mazefactory_aldousbroder import MazeFactoryAldousBroder
from src.maze.factory.mazefactory_binarytree import MazeFactoryBinaryTree
from src.maze.factory.mazefactory_huntandkill import MazeFactoryHuntAndKill
from src.maze.factory.mazefactory_sidewinder import MazeFactorySidewinder
from src.maze.factory.mazefactory_wilson import MazeFactoryWilson
from src.maze.mazehelper import MazeHelper
from src.maze.renderer.ortho_mazerenderer import OrthoMazeRenderer
from src.maze.renderer.point2d import Point2D
from src.maze.renderer.polar_mazerenderer import PolarMazeRenderer


class PyMazesDialog(QtWidgets.QDialog):
    CELL_SIZE = 20


    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = uic.loadUi("mazes.ui", self)
        self.ui.drawMazeButton.clicked.connect(self.onDraw)
        self.ui.widthEdit.setFocus()

        self.draw = False

        self.pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        self.pen.setWidth(2)

        self.brush = QtGui.QBrush(QtGui.QColor(150, 150, 150))

        self.base_x = 20
        self.base_y = 70

        self.factories = self.create_factorylist()

        self.selection_index = 0


    def paintEvent(self, event):
        if self.draw:
            maze_renderer = None
            if self.selection_index < 7:
                maze_renderer = OrthoMazeRenderer(self.get_painter(), self.base_x, self.base_y, self.CELL_SIZE)
            else:
                maze_renderer = PolarMazeRenderer(self.get_painter(), Point2D(200, 200), self.CELL_SIZE*2)
            maze_renderer.render_maze(self.maze);


    def onDraw(self):
        width = int(self.ui.widthEdit.text())
        height = int(self.ui.heightEdit.text())

        self.selection_index = self.ui.algorithmComboBox.currentIndex()
        mazefactory = self.factories[self.selection_index]

        if self.selection_index < 5:
            self.maze = mazefactory.create_maze(width, height)
        elif self.selection_index == 5:
            self.maze = mazefactory.create_maze(5, 5, 'huntAndKillMask.txt')
        else:
            self.maze = mazefactory.create_maze(width, height)

        self.draw = True

        self.update()


    def get_painter(self):
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)

        return painter


    def create_factorylist(self):
        factories = [MazeFactoryBinaryTree(MazeHelper), MazeFactorySidewinder(MazeHelper),
                     MazeFactoryAldousBroder(MazeHelper),
                     MazeFactoryWilson(MazeHelper), MazeFactoryHuntAndKill(MazeHelper),
                     MazeFactoryHuntAndKill(MazeHelper), MazeFactoryEmptyMaze(MazeHelper),
                     MazeFactoryEmptyMaze(MazeHelper)]

        return factories
