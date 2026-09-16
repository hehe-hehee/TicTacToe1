import numpy as np
import csv, pandas as pd

#Board
class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.size = self.rows * self.cols
        #self.board = np.arange(0, self.size).reshape(rows,cols).astype(object) or
        self.board = np.full((self.rows, self.cols), " _ ")

    def game_board(self):
        for i in range (self.rows):
            print(" -" * (self.cols*3 + 1))
            for j in range (self.cols):
                print(" | "+ self.board[i][j], end="")
            print(" | ")
        print(" -" * (self.cols*3 + 1))


b = Board(3,3)
(b.game_board())