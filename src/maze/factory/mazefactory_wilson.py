from src.maze.factory.abstractmazefactory import AbstractMazeFactory
from ..maze import *
from ..mazehelper import *
from ..wallorientation import *
import random


class MazeFactoryWilson(AbstractMazeFactory):


    def __init__(self, mazehelper:AbstractMazeHelper):
        self.path = []
        self.path_complete = False
        self.visited = []
        self.num_visitedcells = 0
        self.mazehelper = mazehelper


    def create_maze(self, maze_width:int, maze_height:int, mask_filename:str = None):
        random.seed()

        maze = Maze(maze_width, maze_height)

        self.visited = [[False for row_idx in range(maze_height)] for col_idx in
                        range(maze_width)]

        # get initial cell
        current_cell = self.mazehelper.find_random_unvisited_cell(maze, self.visited)
        self.visited[current_cell.col_idx][current_cell.row_idx] = True

        self.num_visitedcells = 1

        while self.num_visitedcells < self.mazehelper.get_cellcount(maze):
            self.path = []

            # select an unvisited cell
            current_cell = self.mazehelper.find_random_unvisited_cell(maze, self.visited)
            self.path.append(current_cell)

            self.path_complete = False

            while not self.path_complete:
                neighbour_cell = self.mazehelper.get_random_neighbourcell(maze, current_cell)

                if self.visited[neighbour_cell.col_idx][neighbour_cell.row_idx]:
                    self.process_visited_cell_found(maze, neighbour_cell)
                else:
                    current_cell = self.process_unvisited_cell_found(current_cell, neighbour_cell)

        return maze


    def process_unvisited_cell_found(self, current_cell, neighbour_cell):
        # is neighbour cell already in path? if yes erase loop
        cell_index = self.find_cell_in_path(neighbour_cell)

        if cell_index != -1:
            self.path = self.path[:cell_index]

        self.path.append(neighbour_cell)
        current_cell = neighbour_cell

        return current_cell


    def process_visited_cell_found(self, maze, neighbour_cell):
        self.path_complete = True

        # update maze with path cells
        self.path.append(neighbour_cell)

        for i in range(len(self.path) - 1):
            cell_0 = self.path[i]
            cell_1 = self.path[i + 1]
            orientation = self.mazehelper.get_wall_orientation(cell_0, cell_1)
            self.mazehelper.erase_wall(maze, cell_0.col_idx, cell_0.row_idx, orientation)
            self.visited[cell_0.col_idx][cell_0.row_idx] = True

            self.num_visitedcells += 1


    def find_cell_in_path(self, cell):

        return self.path.index(cell) if cell in self.path else -1
