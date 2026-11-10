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

    def left_diagonal_win(self):
        for i in range(0, self.rows):
            if self.board[0][0] == " _ ":
                continue

            self.win = True
            if self.board[0][0] != self.board[i][i]: 
                self.win = False

            if self.win:
                self.winner = self.board[0][0]
                return self.winner

            
    def right_diagonal_win(self):
        for i in range(0, self.rows):
            if self.board[0][self.cols-1] == " _ ":
                continue

            self.win = True
            if self.board[0][self.cols-1]!=self.board[i][self.cols-1-i] :
                self.win = False
            

            if self.win:
                self.winner =self.board[0][self.cols-1]
                return self.winner
    
    def tie(self): 
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if self.board[i][j] == " _ ":
                    return False #not tie still remaining
        return True
            
class Player(Board):
    def __init__(self,name, symbol):
        self.name = name
        self.symbol = symbol

    def user_input(self):
        position = int(input("Enter your position: "))-1
        if position ==-1 or position>=self.size:
            return "Invalid Position"
        else:
            pos_row = position//self.rows
            pos_col = position%self.cols
            if self.board[pos_row][pos_col] == " _ ":
                self.board[pos_row][pos_col] = self.symbol
                return True
            else:
                print("Position already taken")
                return False

class Play(Condition):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.game_running = True
        self.symbols = [" X ", " O "]
        random.shuffle(self.symbols)
        
        

    def user_play(self):

            player1 = input("Enter the name of Player 1: ").strip().title()
            player2 = input("Enter the name of Player 2: ").strip().title()

            if not player1:
                player1 = "Player 1"
            if not player2:
                player2 = "Player 2"


            self.p1 = Player(player1, self.symbols[0])
            self.p2 = Player(player2, self.symbols[1])
            self.current_player = self.p1

    
    def switch_player(self):
        if self.current_player == self.p1:
            self.current_player = self.p2
        else:
            self.current_player = self.p1

    def check_wins(self):
        winner = (self.horizontal_win() or self.vertical_win() or self.left_diagonal_win() or self.right_diagonal_win())
        if winner: 
            print(f"Congratulations Winner is {self.current_player.name} Symbol {self.current_player.symbol} \n")

        if self.tie(): 
            print("It's a tie!!!\n")


def game():
    p = Play(3,3)
    p.user_play()
    print(p.p1.symbol)
    print(p.p2.symbol)
game()
#b.board[2][1] = "X"
#b.board_display()