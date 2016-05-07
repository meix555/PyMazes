from .abstractmazefactory import AbstractMazeFactory
from ..maze import *
from ..mazehelper import *
from ..wallorientation import *
import random


class MazeFactoryHuntAndKill(AbstractMazeFactory):
    def create_maze(self, cell_size, maze_width, maze_height):
        random.seed()

        self.maze = Maze(cell_size, maze_width, maze_height)

        self.visited = [[False for row_idx in range(maze_height)] for col_idx in
                        range(maze_width)]

        finished = False

        # get first visited cell
        current_cell = MazeHelper.find_random_unvisited_cell(self.maze, self.visited)
        self.visited[current_cell.col_idx][current_cell.row_idx] = True

        while not finished:
            self.compute_path(current_cell)
            finished = self.hunt()

        return self.maze


    def compute_path(self, start_cell):
        path = []
        path.append(start_cell)

        current_cell = start_cell
        path_complete = False

        while not path_complete:
            neighbour_cell = MazeHelper.get_unvisited_random_neighbourcell(self.maze, current_cell, self.visited)
            if neighbour_cell:
                self.visited[neighbour_cell.col_idx][neighbour_cell.row_idx] = True
                MazeHelper.erase_wall_between_cells(self.maze, current_cell, neighbour_cell)
                current_cell = neighbour_cell
            else:
                path_complete = True


    def hunt(self):
        current_cell = self.maze.cells[0][0]

        found_cell, visited_neighbour_cell = self.hunt_for_unvisited_cell_with_visited_neighbour()

        if found_cell and visited_neighbour_cell:
            # $$$
            print('hunt found the cell: {} {} and visited_neighbour_cell: {} {}'
                  .format(found_cell.col_idx, found_cell.row_idx, visited_neighbour_cell.col_idx, visited_neighbour_cell.row_idx))
            return True
        else:
            return True


    def hunt_for_unvisited_cell_with_visited_neighbour(self):
        found_cell = None
        visited_neighbour_cell = None

        try:
            for row_idx in range(self.maze.maze_height):
                for col_idx in range(self.maze.maze_width):

                    test_cell = self.maze.cells[col_idx][row_idx]

                    if self.visited[test_cell.col_idx][test_cell.row_idx]:
                        continue

                    visited_neighbour_cell = MazeHelper.get_visited_random_neighbourcell(self.maze, test_cell,
                                                                                         self.visited)

                    if visited_neighbour_cell:
                        found_cell = test_cell
                        raise BreakIt
        except BreakIt:
            pass

        return (found_cell, visited_neighbour_cell)


class BreakIt(Exception): pass
