from src.maze.factory.abstractmazefactory import AbstractMazeFactory
from ..maze import *
from ..mazehelper import *
from ..wallorientation import *
import random


class MazeFactoryBinaryTree(object):
    def __init__(self, mazehelper):
        self.mazehelper = mazehelper


    def create_maze(self, maze_width: int, maze_height: int, mask_filename: str = None):

        random.seed()

        maze = Maze(maze_width, maze_height)

        # erase east walls in upper row
        for col_idx in range(maze.maze_width - 1):
            self.mazehelper.erase_wall(maze, col_idx, 0, WallOrientation.EAST)

        # erase north walls in right-most column
        for row_idx in range(1, maze.maze_height):
            self.mazehelper.erase_wall(maze, maze.maze_width - 1, row_idx, WallOrientation.NORTH)

        for col_idx in range(maze.maze_width - 1):
            for row_idx in range(1, maze.maze_height):
                if self.erase_north():
                    self.mazehelper.erase_wall(maze, col_idx, row_idx, WallOrientation.NORTH)
                else:
                    self.mazehelper.erase_wall(maze, col_idx, row_idx, WallOrientation.EAST)

        return maze


    def erase_north(self):
        return random.randint(0, 1) == 0
