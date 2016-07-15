from .cell import Cell


class PolarCell(Cell):
    def __init__(self, row_idx, col_idx):

        Cell.__init__(self, row_idx, col_idx)

        self.cw = None  # PolarCell
        self.ccw = None  # PolarCell
        self.inward = None  # PolarCell
        self.outward = []  # array of PolarCell


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

    def print(self):
        print('---------------')

        print('row_idx: {} col_idx: {}'.format(self.row_idx, self.col_idx))
        if self.cw:
            print('cw: {} {}'.format(self.cw.row_idx, self.cw.col_idx))
        else:
            print('cw: None')

        if self.ccw:
            print('ccw: {} {}'.format(self.ccw.row_idx, self.ccw.col_idx))
        else:
            print('ccw: None')

        print('---------------')