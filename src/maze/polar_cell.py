from .cell import Cell


class PolarCell(Cell):
    def __init__(self, row_idx, col_idx):

        self.cw = None  # PolarCell
        self.ccw = None  # PolarCell
        self.inward = None  # PolarCell
        self.outward = []  # array of PolarCell
        self.row_idx = row_idx
        self.col_idx = col_idx


    def get_neighbours(self):
        list = []
        if self.cw:
            list.append(self.cw)

        if self.ccw:
            list.append(self.ccw)

        if self.inward:
            list.append(self.inward)

        if len(self.outward) > 0:
            list.extend(self.outward)
