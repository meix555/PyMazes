from src.maze.factory.abstractmazefactory import AbstractMazeFactory
from ..maze import *
from ..mazehelper import *
from ..wallorientation import *
import random


class MazeFactoryBinaryTree(AbstractMazeFactory):
    def create_maze(self, maze_width:int, maze_height:int, mask_filename:str = None):

        random.seed()

        maze = Maze(maze_width, maze_height)

        # erase east walls in upper row
        for col_idx in range(maze.maze_width - 1):
            MazeHelper.erase_wall(maze, col_idx, 0, WallOrientation.EAST)

        # erase north walls in right-most column
        for row_idx in range(1, maze.maze_height):
            MazeHelper.erase_wall(maze, maze.maze_width - 1, row_idx, WallOrientation.NORTH)

        for col_idx in range(maze.maze_width - 1):
            for row_idx in range(1, maze.maze_height):
                if self.erase_north():
                    MazeHelper.erase_wall(maze, col_idx, row_idx, WallOrientation.NORTH)
                else:
                    MazeHelper.erase_wall(maze, col_idx, row_idx, WallOrientation.EAST)

        return maze


    def erase_north(self):
        return random.randint(0, 1) == 0
