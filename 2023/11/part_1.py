
with open("input.txt", "r") as f:
    lines = f.read().splitlines()

width = len(lines[0])
height = len(lines)

galaxies = []
for y in range(height):
    for x in range(width):
        if lines[y][x] == "#":
            galaxies.append([x, y])

empty_rows = []
for i, row in enumerate(lines):
    if all(x == "." for x in row):
        empty_rows.append(i)

empty_cols = []
for i in range(width):
    if all(x[i] == "." for x in lines):
        empty_cols.append(i)

for row in reversed(empty_rows):
    new_galaxies = []
    for galaxy in galaxies:
        if galaxy[1] > row:
            new_galaxies.append([galaxy[0], galaxy[1] + 1])
        else:
            new_galaxies.append(galaxy)
    galaxies = new_galaxies

for col in reversed(empty_cols):
    new_galaxies = []
    for galaxy in galaxies:
        if galaxy[0] > col:
            new_galaxies.append([galaxy[0] + 1, galaxy[1]])
        else:
            new_galaxies.append(galaxy)
    galaxies = new_galaxies

galaxies.sort(key=lambda x: (x[1], x[0]))

def distance(g1, g2):
    x1, y1 = g1
    x2, y2 = g2
    return abs(x2 - x1) + abs(y2 - y1)

total = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        total += distance(galaxies[i], galaxies[j])

print(f"Total distance: {total}")
