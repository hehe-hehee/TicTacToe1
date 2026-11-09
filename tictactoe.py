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
        self.winner = None
        self.win = False


    def vertical_win(self):
        for i in range (0, self.rows):
            if self.board[i][0] == " _ ":
                continue
            self.win = True

            for j in range (1, self.cols):
                if self.board[i][0] != self.board[i][j]:
                    self.win  = False

            if self.win == True:
                self.winner = self.board[i][0]
                return self.winner

    def horizontal_win(self):
        for i in range(0, self.cols):
            if self.board[0][i] == " _ ":
                continue

            self.win = True
            for j in range (1,self.rows):
                if self.board[0][j]!= self.board[i][j]:
                    self.win = False
            if self.win:
                self.winner = self.board[0][i]
                return self.winner




class Play(Condition):
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
            if self.board[pos_row][pos_col] == " _ ":
                self.board[pos_row][pos_col] = self.player
            else:
                print("Position already taken")



def game():
    p = Play(3,3)
    p.board[0][2]= " X "
    p.board[1][2]= " X "
    p.board[2][2]= " X "

    
    print(p.board_display())
    print(p.player)
    h_win = p.horizontal_win()
    win = p.vertical_win()
    
    print(f"V Winner {win}")
    print(f"H Winner {h_win}")
    #print(p.user_input())
    print(p.board_display())
    

game()
#b.board[2][1] = "X"
#b.board_display()