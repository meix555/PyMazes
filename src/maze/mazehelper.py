from .walltype import *
from .wallorientation import *
import random


class MazeHelper(object):
    @staticmethod
    def erase_wall(maze, col_idx, row_idx, orientation):
        maze.cells[col_idx][row_idx].set_walltype(orientation, WallType.OPEN)

        if orientation == WallOrientation.NORTH:
            if row_idx > 0:
                maze.cells[col_idx][row_idx - 1].set_walltype(WallOrientation.SOUTH, WallType.OPEN)

        if orientation == WallOrientation.EAST:
            if col_idx < maze.maze_width - 1:
                maze.cells[col_idx + 1][row_idx].set_walltype(WallOrientation.WEST, WallType.OPEN)

        if orientation == WallOrientation.SOUTH:
            if row_idx < maze.maze_height - 1:
                maze.cells[col_idx][row_idx + 1].set_walltype(WallOrientation.NORTH, WallType.OPEN)

        if orientation == WallOrientation.WEST:
            if col_idx > 0:
                maze.cells[col_idx - 1][row_idx].set_walltype(WallOrientation.EAST, WallType.OPEN)


    @staticmethod
    def get_randomcell(maze):
        return maze.cells[random.randint(0, maze.maze_width - 1)][random.randint(0, maze.maze_height - 1)]


    @staticmethod
    def get_cellcount(maze):
        return maze.maze_width * maze.maze_height


    @staticmethod
    def get_neighbourcells_dict(maze, cell):

        cells = {}

        if cell.row_idx < maze.maze_height - 1:
            cells[WallOrientation.SOUTH] = maze.cells[cell.col_idx][cell.row_idx + 1]

        if cell.row_idx > 0:
            cells[WallOrientation.NORTH] = maze.cells[cell.col_idx][cell.row_idx - 1]

        if cell.col_idx < maze.maze_width - 1:
            cells[WallOrientation.EAST] = maze.cells[cell.col_idx + 1][cell.row_idx]

        if cell.col_idx > 0:
            cells[WallOrientation.WEST] = maze.cells[cell.col_idx - 1][cell.row_idx]

        return cells


    @staticmethod
    def get_neighbourcells_list(maze, cell):

        cells = []

        if cell.row_idx < maze.maze_height - 1:
            cells.append(maze.cells[cell.col_idx][cell.row_idx + 1])

        if cell.row_idx > 0:
            cells.append(maze.cells[cell.col_idx][cell.row_idx - 1])

        if cell.col_idx < maze.maze_width - 1:
            cells.append(maze.cells[cell.col_idx + 1][cell.row_idx])

        if cell.col_idx > 0:
            cells.append(maze.cells[cell.col_idx - 1][cell.row_idx])

        return cells


    @staticmethod
    def get_random_neighbourcell(maze, cell):
        neighbourcells = MazeHelper.get_neighbourcells_list(maze, cell)

        return neighbourcells[random.randint(0, len(neighbourcells) - 1)]


    @staticmethod
    def get_wall_orientation(cell, neighbourcell):

        orientation = None

        if cell.col_idx + 1 == neighbourcell.col_idx:
            orientation = WallOrientation.EAST
        elif cell.col_idx - 1 == neighbourcell.col_idx:
            orientation = WallOrientation.WEST
        elif cell.row_idx + 1 == neighbourcell.row_idx:
            orientation = WallOrientation.SOUTH
        elif cell.row_idx - 1 == neighbourcell.row_idx:
            orientation = WallOrientation.NORTH

        return orientation
