import unittest

from src.maze.maze import Maze
from src.maze.mazehelper import MazeHelper


class MazeHelperTest(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(3, 3)


    def test_cellcount(self):
        cellcount = MazeHelper.get_cellcount(self.maze)
        self.assertEqual(cellcount, 9, "wrong cell count")
