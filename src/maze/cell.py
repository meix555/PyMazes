from src.maze.walltype import *
from src.maze.wallorientation import *


class Cell(object):
    def __init__(self, size, col_idx, row_idx):
        self.col_idx = col_idx
        self.row_idx = row_idx
        self.visited = False

        self.size = size

        self.walltypes = {WallOrientation.NORTH: WallType.WALL, WallOrientation.EAST: WallType.WALL,
                          WallOrientation.SOUTH: WallType.WALL, WallOrientation.WEST: WallType.WALL}

        self.Matrix = [[(y, x) for x in range(5)] for y in range(5)]