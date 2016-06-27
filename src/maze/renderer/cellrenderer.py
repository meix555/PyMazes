from ..walltype import *
from ..wallorientation import *


class CellRenderer(object):
    def __init__(self, painter, base_x, base_y, cell_size):
        self.painter = painter
        self.base_x = base_x
        self.base_y = base_y
        self.cell_size = cell_size


    def render(self, cell):

        cell_base_x = self.base_x + cell.col_idx * self.cell_size
        cell_base_y = self.base_y + cell.row_idx * self.cell_size

        if cell.masked:
            self.painter.drawRect(cell_base_x, cell_base_y, self.cell_size, self.cell_size)

        if cell.walltypes[WallOrientation.NORTH] == WallType.WALL and cell.row_idx == 0:
            self.painter.drawLine(cell_base_x, cell_base_y, cell_base_x + self.cell_size, cell_base_y)

        if cell.walltypes[WallOrientation.WEST] == WallType.WALL and cell.col_idx == 0:
            self.painter.drawLine(cell_base_x, cell_base_y + self.cell_size, cell_base_x, cell_base_y)

        if cell.walltypes[WallOrientation.EAST] == WallType.WALL:
            self.painter.drawLine(cell_base_x + self.cell_size, cell_base_y, cell_base_x + self.cell_size,
                                  cell_base_y + self.cell_size)

        if cell.walltypes[WallOrientation.SOUTH] == WallType.WALL:
            self.painter.drawLine(cell_base_x + self.cell_size, cell_base_y + self.cell_size, cell_base_x,
                                  cell_base_y + self.cell_size)
