import numpy as np

#Board
class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.size = self.rows * self.cols
        #self.board = np.arange(0, self.size).reshape(rows,cols).astype(object) or
        self.board = np.full((self.rows, self.cols), "_")

