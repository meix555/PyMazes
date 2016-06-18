from src.maze.maze import Maze


class MaskFactory(object):
    @staticmethod
    def create_mask(filename: str):
        mask = []

        f = open(filename, 'r')

        for line in f:
            mask.append([c == '1' for c in line[:-1]])

        return mask


    @staticmethod
    def mask_maze(maze: Maze, mask: list):

        if len(maze.cells) != len(mask):
            raise ValueError('maze and mask must have equal length.')

        for row_idx in range(len(mask)):
            row = mask[row_idx]
            for col_idx in range(len(row)):
                maze.cells[col_idx][row_idx].masked = row[col_idx]

        return maze
