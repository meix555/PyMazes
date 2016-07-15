import math

from PyQt5.QtCore import QRectF

from src.maze.renderer.abstract_mazerenderer import AbstractMazeRenderer
from src.maze.renderer.point2d import Point2D


class PolarMazeRenderer(AbstractMazeRenderer):
    CENTER_DELTA = 70
    ARC_WHOLE_CIRCLE = 16 * 360


    def __init__(self, painter, ring_size):
        self.painter = painter
        self.center = None
        self.ring_size = ring_size


    def render_maze(self, maze):

        center = self.CENTER_DELTA + len(maze.cells) * self.ring_size
        self.center = Point2D(center, center)

        for row_idx in range(1, len(maze.cells)):

            cell_count = len(maze.cells[row_idx])
            theta = 2 * math.pi / cell_count
            inner_radius = row_idx * self.ring_size
            outer_radius = (row_idx + 1) * self.ring_size

            arc_theta = - self.ARC_WHOLE_CIRCLE / cell_count
            arc_rectangle = QRectF(self.center.x - inner_radius, self.center.y - inner_radius,
                                   2 * inner_radius, 2 * inner_radius)

#            for col_idx in [0, 1, 2]: #range(len(maze.cells[row_idx])):
            for col_idx in range(len(maze.cells[row_idx])):

                cell = maze.cells[row_idx][col_idx]

                # theta_cw = (col_idx + 1) * theta
                # arc_theta_ccw = col_idx * arc_theta

                theta_cw = (col_idx + 1) * theta
                arc_theta_ccw = col_idx * arc_theta

                cx = self.center.x + inner_radius * math.cos(theta_cw)
                cy = self.center.y + inner_radius * math.sin(theta_cw)
                dx = self.center.x + outer_radius * math.cos(theta_cw)
                dy = self.center.y + outer_radius * math.sin(theta_cw)

                if cell.inward:
                    self.painter.drawArc(arc_rectangle, arc_theta_ccw, arc_theta)

                if cell.cw:
                    # print('drawing cw line:')
                    # cell.print()
                    self.painter.drawLine(cx, cy, dx, dy)

        # draw outer circle
        outer_radius = len(maze.cells) * self.ring_size
        arc_rectangle = QRectF(self.center.x - outer_radius, self.center.y - outer_radius,
                               2 * outer_radius, 2 * outer_radius)
        self.painter.drawArc(arc_rectangle, 0, self.ARC_WHOLE_CIRCLE)

        self.rendered = True

