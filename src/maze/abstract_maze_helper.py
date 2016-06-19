
class AbstractMazeHelper(object):

    @staticmethod
    def erase_wall(maze, col_idx, row_idx, orientation):
        raise NotImplementedError("Should have implemented this")


    @staticmethod
    def erase_wall_between_cells(maze, cell1, cell2):
        raise NotImplementedError("Should have implemented this")


    # masking! => OK
    @staticmethod
    def get_randomcell(maze):
        raise NotImplementedError("Should have implemented this")


    @staticmethod
    def get_cellcount(maze):
        return maze.maze_width * maze.maze_height


    # masking!
    @staticmethod
    def get_neighbourcells_dict(maze, cell):
        raise NotImplementedError("Should have implemented this")


    # masking!
    @staticmethod
    def get_neighbourcells_list(maze, cell):
        raise NotImplementedError("Should have implemented this")


    # masking nicht nötig!
    @staticmethod
    def get_random_neighbourcell(maze, cell):
        raise NotImplementedError("Should have implemented this")


    # masking nicht nötig!
    @staticmethod
    def get_unvisited_random_neighbourcell(maze, cell, visited):
        raise NotImplementedError("Should have implemented this")

    # masking nicht nötig!
    @staticmethod
    def get_visited_random_neighbourcell(maze, cell, visited):
        raise NotImplementedError("Should have implemented this")


    @staticmethod
    def get_wall_orientation(cell, neighbourcell):
        raise NotImplementedError("Should have implemented this")


    # masking nicht nötig!
    @staticmethod
    def find_random_unvisited_cell(maze, visited):
        raise NotImplementedError("Should have implemented this")