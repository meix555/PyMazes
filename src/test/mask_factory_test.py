from unittest import TestCase

from testfixtures import should_raise

from src.maze.factory.mask_factory import MaskFactory
from src.maze.maze import Maze


class TestMaskFactory(TestCase):
    def test_mask_factory_reads_file(self):
        expected_mask = [[False, False, False, False, False],
                         [False, True, True, True, False],
                         [False, True, True, True, False],
                         [False, True, True, True, False],
                         [False, False, False, False, False]]

        mask = MaskFactory._create_mask('resources/mask01.txt')

        self.assertListEqual(expected_mask, mask)


    @should_raise(ValueError)
    def test_mask_maze_raises_error_when_different_length(self):
        maze = Maze(20, 4, 4)

        mask = [[False, False, False, False, False],
                [False, True, True, True, False],
                [False, True, True, True, False],
                [False, True, True, True, False],
                [False, False, False, False, False]]

        MaskFactory._mask_maze(maze, mask)


    def test_mask_maze_masks_maze_correctly(self):
        maze = Maze(20, 5, 5)
        mask = MaskFactory._create_mask('resources/mask02.txt')

        maze = MaskFactory._mask_maze(maze, mask)

        for row_idx in range(len(mask)):
            row = mask[row_idx]
            for col_idx in range(len(row)):
                self.assertEquals(row[col_idx], maze.cells[col_idx][row_idx].masked,
                                  'col_idx: {}, row_idx: {}'.format(col_idx, row_idx))


    def test_mask_factory_returns_None_if_filename_empty(self):
        mask = MaskFactory._create_mask('')
        self.assertIsNone(mask)


    def test_mask_factory_returns_None_if_filename_None(self):
        mask = MaskFactory._create_mask(None)
        self.assertIsNone(mask)
