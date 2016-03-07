from ..maze import *
from ..mazehelper import *
from ..wallorientation import *
import random


class MazeFactorySidewinder(object):
    def create_maze(self, cell_size, maze_width, maze_height):

        random.seed()

        maze = Maze(cell_size, maze_width, maze_height)

        # erase east walls in upper row
        for col_idx in range(maze.maze_width - 1):
            MazeHelper.erase_wall(maze, col_idx, 0, WallOrientation.EAST)

        run = []

        for row_idx in range(1, maze.maze_height):
            for col_idx in range(maze.maze_width):

                run.append(col_idx)

                if (col_idx < maze.maze_width - 1) and self.erase_east():
                    MazeHelper.erase_wall(maze, col_idx, row_idx, WallOrientation.EAST)
                else:
                    random_idx = random.randint(0, len(run) - 1)
                    MazeHelper.erase_wall(maze, run[random_idx], row_idx, WallOrientation.NORTH)
                    run.clear()

        return maze


    def erase_east(self):
        return random.randint(0, 1) == 0
