

with open("input.txt", "r") as f:
    boards = [b.splitlines() for b in f.read().split("\n\n")]
    flip_boards = []
    for board in boards:
        flip_board = list(zip(*board))
        flip_board = ["".join(row) for row in flip_board]
        flip_boards.append(flip_board)


def one_diff(s1, s2):
    diffs = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diffs += 1
    return diffs == 1


def check_match(rows1, rows2):
    ones = 0
    for r1, r2 in zip(rows1, rows2):
        if one_diff(r1, r2):
            ones += 1
            continue
        if r1 != r2:
            return False
    return ones == 1

total = 0
for board, flip_board in zip(boards, flip_boards):
    this_total = 0
    for i in range(1, len(board)):
        if check_match(board[i:], reversed(board[:i])):
            total += 100*i
            break
    if this_total:
        continue
    for i in range(1, len(flip_board)):
        if check_match(flip_board[i:], reversed(flip_board[:i])):
            total += i
            break
    print(total)
print(total)
                