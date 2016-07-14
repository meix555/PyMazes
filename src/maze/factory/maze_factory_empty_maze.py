import math

from src.maze.factory.abstractmazefactory import AbstractMazeFactory
from src.maze.maze import Maze
from src.maze.polar_cell import PolarCell


class PolarMazeFactory(AbstractMazeFactory):
    CELL_SIZE = 20


    def __init__(self, mazehelper):
        self.mazehelper = mazehelper


    def create_maze(self, maze_width: int, maze_height: int, mask_filename: str = None):
        # self.maze = Maze(maze_height, maze_width)
        self.maze = self.create_polar_maze(maze_width, maze_height)

        self.configure_cells(maze_width, maze_height)

        return self.maze


    def create_polar_maze(self, maze_width, maze_height):
        maze = Maze(maze_height, maze_width)
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
                print('row_idx {}, col_idx {} '.format(row_idx, col_idx))
                cell.cw = self.maze.cells[row_idx][col_idx + 1] if col_idx <  len(self.maze.cells[row_idx]) -1 else self.maze.cells[row_idx][0]
                cell.ccw = self.maze.cells[row_idx][col_idx - 1]

                ratio = len(self.maze.cells[row_idx]) // len(self.maze.cells[row_idx - 1])
                parent = self.maze.cells[row_idx - 1][col_idx // ratio]
                parent.outward.append(cell)
                cell.inward = parent