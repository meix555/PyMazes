from src.maze.factory.abstractmazefactory import AbstractMazeFactory
from src.maze.maze import Maze


class MazeFactoryEmptyMaze(AbstractMazeFactory):
    def __init__(self, mazehelper):
        self.mazehelper = mazehelper


    def create_maze(self, maze_height: int, maze_width: int, mask_filename: str = None):

        self.maze = Maze(maze_height, maze_width)

        return self.maze
