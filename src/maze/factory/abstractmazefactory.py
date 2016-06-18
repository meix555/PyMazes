class AbstractMazeFactory(object):
    def create_maze(self, maze_width:int, maze_height:int, mask_filename:str = None):
        raise NotImplementedError("Should have implemented this")
