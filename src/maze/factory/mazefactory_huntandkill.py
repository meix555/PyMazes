from src.maze.abstract_maze_helper import AbstractMazeHelper
from src.maze.factory.mask_factory import MaskFactory
from .abstractmazefactory import AbstractMazeFactory
from ..maze import *
from ..mazehelper import *


class MazeFactoryHuntAndKill(AbstractMazeFactory):
    def __init__(self, mazehelper):
        self.mazehelper = mazehelper


    def create_maze(self, maze_height: int, maze_width: int, mask_filename: str = None):
        random.seed()

        self.maze = Maze(maze_height, maze_width)

        self.maze = MaskFactory.mask_maze(self.maze, mask_filename)

        self.visited = [[False for _1 in range(maze_height)] for _2 in range(maze_width)]

        current_cell = self.mazehelper.find_random_unvisited_cell(self.maze, self.visited)

        while current_cell:
            self.visited[current_cell.row_idx][current_cell.col_idx] = True
            self.compute_path(current_cell)
            current_cell = self.hunt()

        return self.maze


    def compute_path(self, start_cell):
        current_cell = start_cell
        path_complete = False

        while not path_complete:
            neighbour_cell = self.mazehelper.get_unvisited_random_neighbourcell(self.maze, current_cell, self.visited)

            if neighbour_cell:
                self.visited[neighbour_cell.row_idx][neighbour_cell.col_idx] = True
                self.mazehelper.erase_wall_between_cells(self.maze, current_cell, neighbour_cell)
                current_cell = neighbour_cell
            else:
                path_complete = True


    def hunt(self):
        unvisited_cell, visited_neighbour_cell = self.hunt_for_unvisited_cell_with_visited_neighbour()

        if unvisited_cell and visited_neighbour_cell:
            self.mazehelper.erase_wall_between_cells(self.maze, unvisited_cell, visited_neighbour_cell)

        return unvisited_cell


    def hunt_for_unvisited_cell_with_visited_neighbour(self):
        unvisited_cell = None
        visited_neighbour_cell = None

        try:
            for row_idx in range(self.maze.maze_height):
                for col_idx in range(self.maze.maze_width):

                    test_cell = self.maze.cells[row_idx][col_idx]

                    if self.visited[test_cell.row_idx][test_cell.col_idx] or test_cell.masked:
                        continue

                    visited_neighbour_cell = self.mazehelper.get_visited_random_neighbourcell(self.maze, test_cell,
                                                                                              self.visited)

                    if visited_neighbour_cell:
                        unvisited_cell = test_cell
                        raise BreakIt
        except BreakIt:
            pass

        return unvisited_cell, visited_neighbour_cell


class BreakIt(Exception): pass
