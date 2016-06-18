from .walltype import *
from .wallorientation import *


class Cell(object):
    def __init__(self, size, col_idx, row_idx):
        self.col_idx = col_idx
        self.row_idx = row_idx
        self.visited = False
        self.masked = False

        self.size = size

        self.walltypes = {WallOrientation.NORTH: WallType.WALL, WallOrientation.EAST: WallType.WALL,
                          WallOrientation.SOUTH: WallType.WALL, WallOrientation.WEST: WallType.WALL}


    def set_walltype(self, orientation, walltype):
        self.walltypes[orientation] = walltype


    def is_same_position(self, othercell):
        return self.col_idx == othercell.col_idx and self.row_idx == othercell.row_idx
