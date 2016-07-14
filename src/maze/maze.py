from .cell import Cell


class Maze(object):
    def __init__(self, maze_width, maze_height):
        self.maze_width = maze_width
        self.maze_height = maze_height

        self.cells = [[Cell(row_idx, col_idx) for col_idx in range(self.maze_width)] for row_idx in
                      range(self.maze_height)]
