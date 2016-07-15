import math

from src.maze.factory.abstractmazefactory import AbstractMazeFactory
from src.maze.maze import Maze
from src.maze.polar_cell import PolarCell


class PolarMazeFactory(AbstractMazeFactory):
    CELL_SIZE = 20


    def __init__(self, mazehelper):
        self.mazehelper = mazehelper


    def create_maze(self, maze_width: int, maze_height: int, mask_filename: str = None):
        self.maze = self.create_polar_maze(maze_width, maze_height)

        self.configure_cells(maze_width, maze_height)

        self.visited = [[False for _1 in range(len(self.maze.cells[row_idx]))] for row_idx in range(maze_height)]

        current_cell = self.mazehelper.find_random_unvisited_cell(self.maze, self.visited)
        # print('------------------------------------')
        # self.print_cell('current_cell', current_cell)

        while current_cell:
            self.visited[current_cell.row_idx][current_cell.col_idx] = True
            self.compute_path(current_cell)
            current_cell = self.hunt()
            # current_cell = None

        return self.maze


    def compute_path(self, start_cell):
        # print('Starting compute_path...')
        current_cell = start_cell
        # self.print_cell('current_cell', current_cell)
        path_complete = False

        testcounter = 1

        while not path_complete:
            neighbour_cell = self.mazehelper.get_unvisited_random_neighbourcell(self.maze, current_cell, self.visited)

            if neighbour_cell:
                # self.print_cell('neighbour_cell', neighbour_cell)
                self.visited[neighbour_cell.row_idx][neighbour_cell.col_idx] = True
                self.mazehelper.erase_wall_between_cells(self.maze, current_cell, neighbour_cell)
                testcounter += 1
                current_cell = neighbour_cell

                # path_complete = testcounter == 3

            else:
                path_complete = True


    def hunt(self):
        # print('Starting hunt...')
        unvisited_cell, visited_neighbour_cell = self.hunt_for_unvisited_cell_with_visited_neighbour()

        if unvisited_cell and visited_neighbour_cell:
            self.mazehelper.erase_wall_between_cells(self.maze, unvisited_cell, visited_neighbour_cell)

        return unvisited_cell


    def hunt_for_unvisited_cell_with_visited_neighbour(self):
        unvisited_cell = None
        visited_neighbour_cell = None

        try:
            for row_idx in range(self.maze.maze_height):
                for col_idx in range(len(self.maze.cells[row_idx])):

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


    def print_cell(self, text:str, cell):
        print ('{}: row: {} col: {}'.format(text, cell.row_idx, cell.col_idx))

    # =================================================================================

    def create_polar_maze(self, maze_width, maze_height):
        maze = Maze(maze_width, maze_height)
        maze.cells = [[] for _ in range(maze_height)]
        maze.cells[0].append(PolarCell(0, 0))

        for row_idx in range(1, len(maze.cells)):
            radius = row_idx * self.CELL_SIZE
            circumference = 2 * math.pi * radius

            previous_count = len(maze.cells[row_idx - 1])
            estimated_cell_width = circumference / previous_count
            ratio = round(estimated_cell_width / self.CELL_SIZE)

            cell_count = previous_count * ratio
            for cell_idx in range(cell_count):
                maze.cells[row_idx].append(PolarCell(row_idx, cell_idx))

        return maze


    def configure_cells(self, maze_width, maze_height):
        for row_idx in range(1, maze_height):
            for col_idx in range(len(self.maze.cells[row_idx])):
                cell = self.maze.cells[row_idx][col_idx]

                cw_col_idx = col_idx + 1 if col_idx < len(self.maze.cells[row_idx]) - 1 else 0
                cell.cw = self.maze.cells[row_idx][cw_col_idx]

                cell.ccw = self.maze.cells[row_idx][col_idx - 1]

                ratio = len(self.maze.cells[row_idx]) // len(self.maze.cells[row_idx - 1])
                parent = self.maze.cells[row_idx - 1][col_idx // ratio]
                parent.outward.append(cell)
                cell.inward = parent


class BreakIt(Exception): pass
