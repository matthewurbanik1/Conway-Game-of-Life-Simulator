import random

class Board:
    def __init__(self, length, width):
        self.reset(length,width)
        self.birth_nums = [3]
        self.survive_nums = [2,3]

    def reset(self,height,width):
        self.height = height
        self.width = width
        self.board = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self):
        for r in range(self.height):
            for c in range(self.width):
                if self.board[r][c]: 
                    print("█",end="")
                else:
                    print(" ",end ="")
            print()

    def random_board(self,height,width):
        self.reset(height,width)
        for r in range(self.height):
            for c in range(self.width):
                alive_or_dead = random.randint(0,1)
                self.board[r][c] = True if alive_or_dead == 1 else False

    def cell_state(self,r,c):
        alive_neighbors = 0
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                if (i,j) == (r,c) or i < 0 or i >= self.height or j < 0 or j >= self.width:
                    continue

                if self.board[i][j]:
                    alive_neighbors += 1

        if not self.board[r][c]:
            if alive_neighbors in self.birth_nums:
                return True
            else:
                return False

        else:
            if alive_neighbors not in self.survive_nums:
                return False
            
            else:
                return True


    def next_board_state(self):
        new_state = [[False for _ in range(self.height)] for _ in range(self.width)]
        for r in range(self.height):
            for c in range(self.height):
                new_state[r][c] = self.cell_state(r,c)

        self.board = new_state


if __name__ == "__main__":
    board = Board(3,3)
    board.board = [[False,True,False],[False,True,False],[False,True,False]]
    board.print_board()


    print("Next:")
    board.next_board_state()
    board.print_board()

    