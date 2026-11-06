import numpy as np
import random

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.size = self.rows * self.cols
        self.board = np.full((self.rows, self.cols), " _ ")

    def board_display(self):
        
        for i in range (self.rows):
            print()
            
            for j in range(self.cols):
                print(f" [{self.board[i][j]}] ", end=" ")
            
            print()

class Condition(Board):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)

class Play(Board):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.player = random.choice([" X ", " O "])
        game_running = True

    def user_input(self):
        position = int(input("Enter your position: "))-1
        if position ==-1 or position>=self.size:
            return "Invalid Position"
        else:
            pos_row = position//self.rows
            pos_col = position%self.cols
            if self.board[pos_row][pos_col] == "  ":
                self.board[pos_row][pos_col] = self.player
            else:
                print("Position already taken")



def game():
    p = Play(3,3)
    p.board[2][1]= " X "
    print(p.board_display())
    print(p.player)
    print(p.user_input())
    print(p.board_display())
    

game()
#b.board[2][1] = "X"
#b.board_display()