from ..maze import *
from ..mazehelper import *
from ..wallorientation import *
import random


class MazeFactoryAldousBroder(object):
    def create_maze(self, cell_size, maze_width, maze_height):
        random.seed()

        maze = Maze(cell_size, maze_width, maze_height)

        visited = [[False for row_idx in range(maze_height)] for col_idx in
                   range(maze_width)]

        current_cell = MazeHelper.get_randomcell(maze)
        visited[current_cell.col_idx][current_cell.row_idx] = True
        num_visited_cells = 1

        while num_visited_cells < MazeHelper.get_cellcount(maze):
            # choose neighbour cell randomly
            neighbour_cells = MazeHelper.get_neighbourcells_dict(maze, current_cell)

            random_orientation = random.choice(list(neighbour_cells.keys()))
            next_cell = neighbour_cells[random_orientation]

            # process neighbour cell
            if not visited[next_cell.col_idx][next_cell.row_idx]:
                MazeHelper.erase_wall(maze, current_cell.col_idx, current_cell.row_idx, random_orientation)
                visited[next_cell.col_idx][next_cell.row_idx] = True
                num_visited_cells += 1

            current_cell = next_cell

        return maze
