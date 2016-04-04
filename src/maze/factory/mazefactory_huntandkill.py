from .abstractmazefactory import AbstractMazeFactory
from ..maze import *
from ..mazehelper import *
from ..wallorientation import *
import random


class MazeFactoryHuntAndKill(object):
    def create_maze(self, cell_size, maze_width, maze_height):
        random.seed()

        maze = Maze(cell_size, maze_width, maze_height)

        self.visited = [[False for row_idx in range(maze_height)] for col_idx in
                        range(maze_width)]

        finished = False

        # get first visited cell
        current_cell = MazeHelper.find_random_unvisited_cell(maze, self.visited)
        self.visited[current_cell.col_idx][current_cell.row_idx] = True

        self.path = []
        self.path.append(current_cell)

        while not finished:
            self.compute_path()
            finished = self.hunt()

        return maze


    def compute_path(self):
        pass


    def hunt(self):
        return True
