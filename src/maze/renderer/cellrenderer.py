from ..walltype import *
from ..wallorientation import *


class CellRenderer(object):
    def __init__(self, painter, base_x, base_y):
        self.painter = painter
        self.base_x = base_x
        self.base_y = base_y


    def render(self, cell):

        cell_base_x = self.base_x + cell.col_idx * cell.size
        cell_base_y = self.base_y + cell.row_idx * cell.size

        if cell.masked:
            self.painter.drawRect(cell_base_x, cell_base_y, cell.size, cell.size)

        if cell.walltypes[WallOrientation.NORTH] == WallType.WALL:
            self.painter.drawLine(cell_base_x, cell_base_y, cell_base_x + cell.size, cell_base_y)

        if cell.walltypes[WallOrientation.EAST] == WallType.WALL:
            self.painter.drawLine(cell_base_x + cell.size, cell_base_y, cell_base_x + cell.size,
                                  cell_base_y + cell.size)

        if cell.walltypes[WallOrientation.SOUTH] == WallType.WALL:
            self.painter.drawLine(cell_base_x + cell.size, cell_base_y + cell.size, cell_base_x,
                                  cell_base_y + cell.size)

        if cell.walltypes[WallOrientation.WEST] == WallType.WALL:
            self.painter.drawLine(cell_base_x, cell_base_y + cell.size, cell_base_x, cell_base_y)
