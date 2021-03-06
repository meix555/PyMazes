import random

from src.maze.abstract_maze_helper import AbstractMazeHelper
from .walltype import *
from .wallorientation import *


class OrthoMazeHelper(AbstractMazeHelper):
    @staticmethod
    def erase_wall(maze, row_idx, col_idx, orientation):
        maze.cells[row_idx][col_idx].set_walltype(orientation, WallType.OPEN)

        try:

            if orientation == WallOrientation.WEST:
                if col_idx > 0:
                    maze.cells[row_idx][col_idx - 1].set_walltype(WallOrientation.EAST, WallType.OPEN)

            if orientation == WallOrientation.SOUTH:
                if row_idx < maze.maze_height - 1:
                    maze.cells[row_idx + 1][col_idx].set_walltype(WallOrientation.NORTH, WallType.OPEN)

            if orientation == WallOrientation.EAST:
                if col_idx < maze.maze_width - 1:
                    maze.cells[row_idx][col_idx + 1].set_walltype(WallOrientation.WEST, WallType.OPEN)

            if orientation == WallOrientation.NORTH:
                if row_idx > 0:
                    maze.cells[row_idx - 1][col_idx].set_walltype(WallOrientation.SOUTH, WallType.OPEN)

        except IndexError:
            print('IndexError row_idx: {}, col_idx: {}'.format(row_idx, col_idx))


    @staticmethod
    def erase_wall_between_cells(maze, cell1, cell2):
        orientation = OrthoMazeHelper.get_wall_orientation(cell1, cell2)
        OrthoMazeHelper.erase_wall(maze, cell1.row_idx, cell1.col_idx, orientation)


    @staticmethod
    def get_randomcell(maze):

        cell = None

        found = False

        while not found:
            cell = maze.cells[random.randint(0, maze.maze_height - 1)][random.randint(0, maze.maze_width - 1)]
            found = not cell.masked

        return cell


    @staticmethod
    def get_neighbourcells_dict(maze, cell):

        cells = {}

        if cell.row_idx < maze.maze_height - 1:
            cells[WallOrientation.SOUTH] = maze.cells[cell.row_idx + 1][cell.col_idx]

        if cell.row_idx > 0:
            cells[WallOrientation.NORTH] = maze.cells[cell.row_idx - 1][cell.col_idx]

        if cell.col_idx < maze.maze_width - 1:
            cells[WallOrientation.EAST] = maze.cells[cell.row_idx][cell.col_idx + 1]

        if cell.col_idx > 0:
            cells[WallOrientation.WEST] = maze.cells[cell.row_idx][cell.col_idx - 1]

        return cells


    @staticmethod
    def get_neighbourcells_list(maze, cell):

        cells = []

        if cell.row_idx < maze.maze_height - 1:
            cells.append(maze.cells[cell.row_idx + 1][cell.col_idx])

        if cell.row_idx > 0:
            cells.append(maze.cells[cell.row_idx - 1][cell.col_idx])

        if cell.col_idx < maze.maze_width - 1:
            cells.append(maze.cells[cell.row_idx][cell.col_idx + 1])

        if cell.col_idx > 0:
            cells.append(maze.cells[cell.row_idx][cell.col_idx - 1])

        unmasked_cells = [cell for cell in cells if not cell.masked]

        return unmasked_cells


    @staticmethod
    def get_random_neighbourcell(maze, cell):
        neighbourcells = OrthoMazeHelper.get_neighbourcells_list(maze, cell)

        return neighbourcells[random.randint(0, len(neighbourcells) - 1)]


    @staticmethod
    def get_unvisited_random_neighbourcell(maze, cell, visited):
        neighbourcells = OrthoMazeHelper.get_neighbourcells_list(maze, cell)

        unvisitedcells = [cell for cell in neighbourcells if not visited[cell.row_idx][cell.col_idx]]

        if unvisitedcells:
            random.seed()
            return unvisitedcells[random.randint(0, len(unvisitedcells) - 1)]
        else:
            return None


    @staticmethod
    def get_visited_random_neighbourcell(maze, cell, visited):
        neighbourcells = OrthoMazeHelper.get_neighbourcells_list(maze, cell)

        visitedcells = [cell for cell in neighbourcells if visited[cell.row_idx][cell.col_idx]]

        if visitedcells:
            random.seed()
            return visitedcells[random.randint(0, len(visitedcells) - 1)]
        else:
            return None


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


    @staticmethod
    def find_random_unvisited_cell(maze, visited):
        cell = None

        found = False

        while not found:
            cell = OrthoMazeHelper.get_randomcell(maze)
            found = not visited[cell.row_idx][cell.col_idx]

        return cell
