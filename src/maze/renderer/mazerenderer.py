from .cellrenderer import CellRenderer


class MazeRenderer(object):
    def __init__(self, painter, base_x, base_y, cell_size):
        self.cellrenderer = CellRenderer(painter, base_x, base_y, cell_size)

    def render(self, maze):

        for col_idx in range(0, maze.maze_width):
            for row_idx in range(0, maze.maze_height):
                self.cellrenderer.render(maze.cells[col_idx][row_idx])
