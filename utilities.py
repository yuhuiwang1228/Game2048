import random
from copy import deepcopy
        
class game:
    def __init__(self,rows):
        self.rows = rows
        self.board = [[0 for _ in range(rows)] for _ in range(rows)]

    def is_full(self):
        return all(all(row) for row in self.board)
    
    def check_valid_input(self,move):
        if move not in ['w', 's', 'a', 'd']:
            raise ValueError("Invalid input! Please enter 'w', 's', 'a', or 'd'.")

    def add_new(self):
        while True:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.rows - 1)
            if self.board[row][col] == 0:
                self.board[row][col] = 2
                break
    
    def check_win(self):
        return any(any(cell == 2048 for cell in row) for row in self.board)

    def print_board(self):
        print()
        for row in self.board:
            print(" ".join("{:4}".format(num) if num!=0 else '   .' for num in row))
        print()


    def play(self, direction):
        board = deepcopy(self.board)
        if direction == 'w':
            self.board = self.rotate(self.merge(self.compress(self.rotate(board,3))),1)
        elif direction == 's':
            self.board = self.rotate(self.merge(self.compress(self.rotate(board,1))),3)
        elif direction == 'a':
            self.board = self.merge(self.compress(board))
        elif direction == 'd':
            self.board = self.rotate(self.merge(self.compress(self.rotate(board,2))),2)

    def compress(self, board):
        for row in board:
            i = 0
            for j in range(self.rows):
                if row[j]!=0:
                    row[i],row[j] = row[j],row[i]
                    i += 1
        return board

    def merge(self, board):
        for row in board:
            for j in range(self.rows):
                if row[j]==0:
                    break
                if j>0 and row[j]==row[j-1]:
                    row[j-1] *= 2
                    row[j] = 0
        self.compress(board)
        return board

    def rotate(self, board, times):
        # Rotate the board 90 degrees clockwise 'times' times
        for _ in range(times):
            board = zip(*board[::-1])
            board = [list(pair) for pair in board]
        return board
    
    def reverse_rotate(self, board, times):
        for _ in range(times):
            board = zip(*board[::-1])
            board = [list(pair) for pair in board]
        return board
