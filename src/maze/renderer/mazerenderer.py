from .cellrenderer import CellRenderer


class MazeRenderer(object):
    def __init__(self, painter, baseX, baseY):
        self.cellrenderer = CellRenderer(painter, baseX, baseY)

    def render(self, maze):

        for colIdx in range(0, maze.mazeWidth):
            for rowIdx in range(0, maze.mazeHeight):
                self.cellrenderer.render(maze.cells[colIdx][rowIdx])
