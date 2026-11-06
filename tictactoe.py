import numpy as np

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.size = self.rows * self.cols
        self.board = np.full((self.rows, self.cols), "_")

    def board_display(self):
        print("-" *(self.rows*7+ (self.rows-1)))
        for i in range (self.rows):
            
            for j in range(self.cols):
                print(f" [ {self.board[i][j]} ] ", end=" ")
            
            print()
        print("-" *(self.cols*7+ (self.rows-1)))


b = Board(rows=3, cols=3)
b.board[2][1] = "X"
b.board_display()