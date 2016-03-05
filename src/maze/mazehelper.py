from .walltype import *
from .wallorientation import *


class MazeHelper(object):
    @staticmethod
    def erase_wall(maze, col_idx, row_idx, orientation):
        maze.cells[col_idx][row_idx].set_walltype(orientation, WallType.OPEN)

        if orientation == WallOrientation.NORTH:
            if row_idx > 0:
                maze.cells[col_idx][row_idx - 1].set_walltype(WallOrientation.SOUTH, WallType.OPEN)

        if orientation == WallOrientation.EAST:
            if col_idx < maze.maze_width - 1:
                maze.cells[col_idx + 1][row_idx].set_walltype(WallOrientation.WEST, WallType.OPEN)

        if orientation == WallOrientation.SOUTH:
            if row_idx < maze.maze_height - 1:
                maze.cells[col_idx][row_idx + 1].set_walltype(WallOrientation.NORTH, WallType.OPEN)

        if orientation == WallOrientation.WEST:
            if col_idx > 0:
                maze.cells[col_idx - 1][row_idx].set_walltype(WallOrientation.EAST, WallType.OPEN)
