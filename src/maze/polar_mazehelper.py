import random

from src.maze.abstract_maze_helper import AbstractMazeHelper


class PolarMazeHelper(AbstractMazeHelper):
    def __init__(self):
        pass


    @staticmethod
    def erase_wall_between_cells(maze, cell1, cell2):
        PolarMazeHelper.erase_polar_neighbourhood(cell1, cell2)
        PolarMazeHelper.erase_polar_neighbourhood(cell2, cell1)


    @staticmethod
    def erase_polar_neighbourhood(cell1, cell2):

        # print('START erase_polar_neighbourhood with ')
        # PolarMazeHelper.print_cell('cell1', cell1)
        # PolarMazeHelper.print_cell('cell2', cell2)

        if cell1.cw == cell2:
            # print('  erasing cw')
            cell1.cw = None

        if cell1.ccw == cell2:
            # print('  erasing ccw')
            cell1.ccw = None

        if cell1.inward == cell2:
            # print('  erasing inward')
            cell1.inward = None

        if cell2 in cell1.outward:
            # print('  erasing outward')
            cell1.outward.remove(cell2)


    @staticmethod
    def print_cell(text: str, cell):
        print('{}:'.format(text))
        cell.print()


    @staticmethod
    def get_randomcell(maze):

        cell = None
        found = False

        while not found:
            row_idx = random.randint(0, maze.maze_height - 1)
            col_idx = random.randint(0, len(maze.cells[row_idx]) - 1)

            cell = maze.cells[row_idx][col_idx]
            found = not cell.masked

        return cell


    @staticmethod
    def find_random_unvisited_cell(maze, visited):
        cell = None

        found = False

        while not found:
            cell = PolarMazeHelper.get_randomcell(maze)
            found = not visited[cell.row_idx][cell.col_idx]

        return cell


    @staticmethod
    def get_unvisited_random_neighbourcell(maze, cell, visited):
        neighbourcells = PolarMazeHelper.get_neighbourcells_list(maze, cell)

        unvisitedcells = [cell for cell in neighbourcells if not visited[cell.row_idx][cell.col_idx]]

        if unvisitedcells:
            random.seed()
            return unvisitedcells[random.randint(0, len(unvisitedcells) - 1)]
        else:
            return None


    @staticmethod
    def get_neighbourcells_list(maze, cell):

        cells = []

        if cell.cw:
            cells.append(cell.cw)

        if cell.ccw:
            cells.append(cell.ccw)

        if cell.inward:
            cells.append(cell.inward)

        if cell.outward and len(cell.outward) > 0:
            cells.extend(cell.outward)

        unmasked_cells = [cell for cell in cells if not cell.masked]

        return unmasked_cells


    @staticmethod
    def get_visited_random_neighbourcell(maze, cell, visited):
        neighbourcells = PolarMazeHelper.get_neighbourcells_list(maze, cell)

        visitedcells = [cell for cell in neighbourcells if visited[cell.row_idx][cell.col_idx]]

        if visitedcells:
            random.seed()
            return visitedcells[random.randint(0, len(visitedcells) - 1)]
        else:
            return None
