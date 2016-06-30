from src.maze.factory.abstractmazefactory import AbstractMazeFactory
from ..maze import *
from ..ortho_mazehelper import *
from ..wallorientation import *
import random


class MazeFactorySidewinder(AbstractMazeFactory):

    def __init__(self, mazehelper):
        self.mazehelper = mazehelper

    def create_maze(self, maze_height: int, maze_width: int, mask_filename: str = None):

        random.seed()

        maze = Maze(maze_height, maze_width)

        # erase east walls in upper row
        for col_idx in range(maze.maze_width - 1):
            self.mazehelper.erase_wall(maze, 0, col_idx, WallOrientation.EAST)

        run = []

        for row_idx in range(1, maze.maze_height):
            for col_idx in range(maze.maze_width):

                run.append(col_idx)

                if (col_idx < maze.maze_width - 1) and self.erase_east():
                    OrthoMazeHelper.erase_wall(maze, row_idx, col_idx, WallOrientation.EAST)
                else:
                    random_idx = random.randint(0, len(run) - 1)
                    OrthoMazeHelper.erase_wall(maze, row_idx, run[random_idx], WallOrientation.NORTH)
                    run.clear()

        return maze


    def erase_east(self):
        return random.randint(0, 1) == 0
