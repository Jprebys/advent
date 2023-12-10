
with open("input.txt", "r") as f:
    lines = f.read().splitlines()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            start = x, y

adj = {
    "|": ((0, -1), (0, 1)),
    "-": ((-1, 0), (1, 0)),
    "F": ((1, 0), (0, 1)),
    "7": ((-1, -0), (0, 1)),
    "L": ((1, 0), (0, -1)),
    "J": ((-1, 0), (0, -1))
}

visited = {start}
typ = "7"

def add(pos, move):
    return (pos[0] + move[0], pos[1] + move[1])

pos = add(start, adj[typ][0])

moves = 1
while True:
    visited.add(pos)
    x, y = pos
    typ = lines[y][x]
    move1, move2 = adj[typ]
    next1, next2 = add(pos, move1), add(pos, move2)
    # print(next1, next2)
    # print(visited)


    if next1 not in visited:
        pos = next1
    elif next2 not in visited:
        pos = next2
    elif next1 in visited and next2 in visited:
        break

# Visited == main loop

print(f"Loop length: {len(visited)}")

width = len(lines[0])
height = len(lines)

edges = {"|", "L", "J"}

inside = 0
for y in range(height):
    walls = 0
    for x in range(width):
        spot = x, y
        if spot in visited:
            if lines[y][x] in edges:
                walls += 1
        else:
            if walls % 2:
                inside += 1

print(f"Inside count: {inside}")



