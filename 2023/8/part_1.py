
paths = []
with open("input.txt", "r") as f:
    moves = next(f).strip()
    next(f)
    for line in f:
        key = line[:3]
        ends = line[line.index("(")+1:line.index(")")]
        paths.append((key, ends.split(", ")))

end = "ZZZ"
start = "AAA"
paths = dict(paths)
steps = 0
idx = 0
pos = start
n_moves = len(moves)

while pos != end:
    left, right = paths[pos]
    pos = left if moves[idx] == "L" else right
    idx = (idx + 1) % n_moves
    steps += 1

print(steps)

