from src.maze.renderer.abstract_mazerenderer import AbstractMazeRenderer

from PyQt5.QtCore import QRectF

from math import pi as PI
from math import cos
from math import sin


class PolarMazeRenderer(AbstractMazeRenderer):
    def __init__(self, painter, center, ring_size):
        self.painter = painter
        self.center = center
        self.ring_size = ring_size
        print('init')


    def render_maze(self, maze):

        # self.painter.drawEllipse(self.center.x, self.center.y, self.ring_size, self.ring_size)

        for row_idx in range(len(maze.cells)):  # maze.maze_height

            cell_count = len(maze.cells[row_idx])
            theta = 2 * PI / cell_count
            inner_radius = row_idx * self.ring_size
            outer_radius = (row_idx + 1) * self.ring_size

            theta_stupid = 16 * 360 / cell_count

            rectangle = QRectF(self.center.x - outer_radius,
                               self.center.y - outer_radius,
                               2 * outer_radius,
                               2 * outer_radius)

            for col_idx in range(len(maze.cells[row_idx])):
                print('drawing cell {}:'.format(col_idx))

                theta_ccw = col_idx * theta
                theta_cw = (col_idx + 1) * theta

                theta_stupid_ccw = col_idx * theta_stupid
                theta_stupid_cw = (col_idx + 1) * theta_stupid

                ax = self.center.x + inner_radius * cos(theta_ccw)
                ay = self.center.y + inner_radius * sin(theta_ccw)
                bx = self.center.x + outer_radius * cos(theta_ccw)
                by = self.center.y + outer_radius * sin(theta_ccw)
                cx = self.center.x + inner_radius * cos(theta_cw)
                cy = self.center.y + inner_radius * sin(theta_cw)
                dx = self.center.x + outer_radius * cos(theta_cw)
                dy = self.center.y + outer_radius * sin(theta_cw)

                # self.painter.drawLine(ax, ay, cx, cy)
                self.painter.drawArc(rectangle, theta_stupid_ccw, theta_stupid)
                self.painter.drawLine(cx, cy, dx, dy)

                if row_idx == maze.maze_height - 1:
                    # self.painter.drawLine(bx, by, dx, dy)
                    # self.painter.drawRect(rectangle)
                    self.painter.drawArc(rectangle, theta_stupid_ccw, theta_stupid)
