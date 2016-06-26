from src.maze.renderer.abstract_mazerenderer import AbstractMazeRenderer

from math import pi as PI


class PolarMazeRenderer(AbstractMazeRenderer):
    def __init__(self, painter, center, ring_size):
        self.painter = painter
        self.center = center
        self.ring_size = ring_size
        print('init')


    def render_maze(self, maze):
        cell_count = maze.maze_width

        theta = 2 * PI / cell_count

        self.painter.drawEllipse(self.center.x, self.center.y, self.ring_size, self.ring_size)

        for row_idx in range(1):  # maze.maze_height
            for col_idx in range(maze.maze_width):
                pass


