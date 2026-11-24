import random

class Board:
    def __init__(self, length=3, width=3):
        self.reset(length,width)
        self.birth_nums = [3]
        self.survive_nums = [2,3]

    def reset(self,height,width):
        self.height = height
        self.width = width
        self.board = [[False for _ in range(width)] for _ in range(height)]

    def is_empty(self):
        for row in self.board:
            for cell in row:
                if cell:
                    return False
        return True

    def print_board(self):
        for row in self.board:
            print(*("■" if cell else " " for cell in row), sep = " ")

    def random_board(self):
        self.reset(board.height, board.width)
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

    def run(self,runs=10):
        for _ in range(runs):
            print("Next:")
            self.next_board_state()
            self.print_board()
            if self.is_empty():
                print("Empty board, terminating run")
                break
        print("Runs complete")

    def user_menu(self):
        print("""
        1. Run Random Board
        2. Set Board Size
        """)
        try:
            menu_choice = int(input())
            match menu_choice:
                case 1:
                    board.random_board()
                    board.run()
                case 2:
                    print("Please enter 2 integers seperated by a space (Ex. 3 3)")
                    try:
                        board_size = input()
                        board.height, board.width = (int(board_size[0]), int(board_size[2]))
                        print("Board size set to", board.height, "x", board.width)
                    except:
                        print("Invalid input.")
        except:
            print("Please input an integer 1-2.")

if __name__ == "__main__":
    board = Board()
    while True:
        board.user_menu()
    