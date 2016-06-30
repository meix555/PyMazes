from src.maze.factory.abstractmazefactory import AbstractMazeFactory
from ..maze import *
from ..ortho_mazehelper import *
from ..wallorientation import *
import random


class MazeFactoryBinaryTree(object):
    def __init__(self, mazehelper):
        self.mazehelper = mazehelper


    def create_maze(self, maze_height: int, maze_width: int, mask_filename: str = None):

        random.seed()

        maze = Maze(maze_height, maze_width)

        # erase east walls in upper row
        for col_idx in range(maze.maze_width - 1):
            self.mazehelper.erase_wall(maze, 0, col_idx, WallOrientation.EAST)

        # erase north walls in right-most column
        for row_idx in range(1, maze.maze_height):
            self.mazehelper.erase_wall(maze, row_idx, maze.maze_width - 1, WallOrientation.NORTH)

        for row_idx in range(1, maze.maze_height):
            for col_idx in range(maze.maze_width - 1):
                if self.erase_north():
                    self.mazehelper.erase_wall(maze, row_idx, col_idx, WallOrientation.NORTH)
                else:
                    self.mazehelper.erase_wall(maze, row_idx, col_idx, WallOrientation.EAST)

        return maze


    def erase_north(self):
        return random.randint(0, 1) == 0
