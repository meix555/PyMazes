from src.maze.factory.abstractmazefactory import AbstractMazeFactory
from src.maze.maze import Maze


class MazeFactoryEmptyMaze(AbstractMazeFactory):
    def __init__(self, mazehelper):
        self.mazehelper = mazehelper


    def create_maze(self, maze_width: int, maze_height: int, mask_filename: str = None):

        self.maze = Maze(maze_width, maze_height)

        return self.maze
