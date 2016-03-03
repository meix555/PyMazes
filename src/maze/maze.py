import numpy as np
from .cell import Cell

class Maze(object):

    def __init__(self, cellSize, mazeWidth, mazeHeight):

        self.cellSize = cellSize
        self.mazeWidth = mazeWidth
        self.mazeHeight = mazeHeight

        self.cells = [[Cell(self.cellSize, colIdx, rowIdx) for rowIdx in range(self.mazeHeight)] for colIdx in range(self.mazeWidth)]
