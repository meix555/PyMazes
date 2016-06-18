from src.maze.maze import Maze


class MaskFactory(object):
    @classmethod
    def _create_mask(cls, filename: str):

        mask = None

        if filename:
            mask = []
            f = open(filename, 'r')
            for line in f:
                mask.append([c == '1' for c in line[:-1]])

        return mask


    @classmethod
    def _mask_maze(cls, maze: Maze, mask: list):

        if len(maze.cells) != len(mask):
            raise ValueError('maze and mask must have equal length.')

        for row_idx in range(len(mask)):
            row = mask[row_idx]
            for col_idx in range(len(row)):
                maze.cells[col_idx][row_idx].masked = row[col_idx]

        return maze


    @classmethod
    def mask_maze(cls, maze: Maze, filename:str):
        mask = cls._create_mask(filename)
        return cls._mask_maze(maze, mask) if mask else maze