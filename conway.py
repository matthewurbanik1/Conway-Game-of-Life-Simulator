import random

class Board:
    def __init__(self, length):
        self.reset(length)

    def reset(self,length):
        self.length = length
        self.board = [[False for _ in range(length)] for _ in range(length)]

    def print_board(self):
        for r in range(self.length):
            for c in range(self.length):
                if self.board[r][c]: 
                    print("█",end="")
                else:
                    print(" ",end ="")
            print()

    def random_board(self,length):
        self.reset(length)
        for r in range(self.length):
            for c in range(self.length):
                alive_or_dead = random.randint(0,1)
                self.board[r][c] = True if alive_or_dead == 1 else False

            

if __name__ == "__main__":
    board = Board(5)
    board.random_board(5)
    board.print_board()