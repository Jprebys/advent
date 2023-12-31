

with open("input.txt", "r") as f:
    boards = [b.splitlines() for b in f.read().split("\n\n")]
    flip_boards = []
    for board in boards:
        flip_board = list(zip(*board))
        flip_board = ["".join(row) for row in flip_board]
        flip_boards.append(flip_board)

def check_match(rows1, rows2):
    for r1, r2 in zip(rows1, rows2):
        if r1 != r2:
            return False
    return True
total = 0
for board, flip_board in zip(boards, flip_boards):
    this_total = 0
    for i in range(1, len(board)):
        if board[i] == board[i-1]:
            if check_match(board[i:], reversed(board[:i])):
                total += 100*i
                break
    if this_total:
        continue
    for i in range(1, len(flip_board)):
        if flip_board[i] == flip_board[i-1]:
            if check_match(flip_board[i:], reversed(flip_board[:i])):
                total += i
                break
print(total)
                