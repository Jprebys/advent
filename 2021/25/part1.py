EMPTY = '.'
EAST = '>'
SOUTH = 'v'

def create_empty(width, height):
    board = []
    for _ in range(height):
        board.append([EMPTY for _ in range(width)])
    return board

class SeaFloor:
    def __init__(self, filename):
        self.board = []
        with open(filename, "r") as f:
            for row in f:
                self.board.append(list(row.strip()))
        self.width = len(self.board[0])
        self.height = len(self.board)

        self.print()
        self.turns = 1

    def move(self):
        change = False
        next_board = create_empty(self.width, self.height)
        for y, row in enumerate(self.board):
            for x, cucumber in enumerate(row):
                if cucumber == EAST:
                    if self.board[y][(x + 1) % self.width] == EMPTY:
                        change = True
                        next_board[y][(x + 1) % self.width] = EAST
                    else:
                        next_board[y][x] = EAST

        for y in range(self.height):
            for x in range(self.width):
                if next_board[y][x] == EAST and self.board[y][x] == EMPTY:
                    self.board[y][x] = EAST
                if next_board[y][x] == EMPTY and self.board[y][x] == EAST:
                    self.board[y][x] = EMPTY



        for y, row in enumerate(self.board):
            for x, cucumber in enumerate(row):
                if cucumber == SOUTH:
                    if self.board[(y + 1) % self.height][x] == EMPTY:
                        change = True
                        next_board[(y + 1) % self.height][x] = SOUTH
                    else:
                        next_board[y][x] = SOUTH
        self.board = next_board
        return change
    
    def print(self):
        for row in self.board:
            for cucumber in row:
                print(cucumber, end='')
            print()
        print()
    
    def run(self):
        print()
        while self.move():
            self.turns += 1

        return self.turns




if __name__ == "__main__":
    print(SeaFloor("input1.txt").run())