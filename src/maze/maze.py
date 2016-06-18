import numpy as np
from .cell import Cell


class Maze(object):
    def __init__(self, maze_width, maze_height):
        self.maze_width = maze_width
        self.maze_height = maze_height

        self.cells = [[Cell(col_idx, row_idx) for row_idx in range(self.maze_height)] for col_idx in
                      range(self.maze_width)]
