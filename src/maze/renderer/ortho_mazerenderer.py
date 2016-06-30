from src.maze.renderer.abstract_mazerenderer import AbstractMazeRenderer
from .ortho_cellrenderer import OrthoCellRenderer


class OrthoMazeRenderer(AbstractMazeRenderer):
    def __init__(self, painter, base_x, base_y, cell_size):
        self.cellrenderer = OrthoCellRenderer(painter, base_x, base_y, cell_size)


    def render_maze(self, maze):
        for row_idx in range(0, maze.maze_height):
            for col_idx in range(0, maze.maze_width):
                self.cellrenderer.render(maze.cells[row_idx][col_idx])
