import math
import itertools

paths = {}
starts = []
with open("input.txt", "r") as f:
    moves = next(f).strip()
    next(f)
    for line in f:
        key = line[:3]
        if key[-1] == "A":
            starts.append(key)
        ends = line[line.index("(")+1:line.index(")")]
        paths[key] = ends.split(", ")

paths = dict(paths)
completions = []
n_moves = len(moves)


for start in starts:
    pos = start
    steps = 0
    idx = 0
    this_complete = []
    while len(this_complete) < 10:
        # Hopefully 10 passes through finish is enough
        while pos[-1] != "Z":
            left, right = paths[pos]
            pos = left if moves[idx] == "L" else right
            idx = (idx + 1) % n_moves
            steps += 1
        this_complete.append(steps)
        left, right = paths[pos]
        pos = left if moves[idx] == "L" else right
        idx = (idx + 1) % n_moves
        steps += 1
    completions.append(this_complete)

print(min(math.lcm(*row) for row in itertools.product(*completions)))
