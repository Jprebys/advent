import functools

with open("input.txt") as f:
    lines = f.read().splitlines()

print(lines)

left = (-1, 0)
right = (1, 0)
up = (0, -1)
down = (0, 1)

start = (0, 0)
dir = down

angle = {
    "/": {up: right, right: up, left: down, down: left},
    "\\": {left: up, up: left, right: down, down: right}
}

width = len(lines[0])
height = len(lines)


def off_board(posx, posy):
    return posx < 0 or posx >= width or posy < 0 or posy >= height

_cache = set()

@functools.cache
def move(xpos, ypos, dirx, diry):

    if (xpos, ypos, dirx, diry) in _cache:
        return set()
    _cache.add((xpos, ypos, dirx, diry) )


    energized = set()
    while True:

        xpos = xpos + dirx
        ypos = ypos + diry
        direction = dirx, diry

        if off_board(xpos, ypos):
            return energized
    
        spot = lines[ypos][xpos]
        energized.add((xpos, ypos))
        if spot in angle:
            dirx, diry = angle[spot][direction]

        elif (direction == up or direction == down) and spot == "-":
            energized |= move(xpos, ypos, *right)
            energized |= move(xpos, ypos, *left)
            return energized
        elif (direction == left or direction == right) and spot == "|":
            energized |= move(xpos, ypos, *up)
            energized |= move(xpos, ypos, *down)
            return energized

max = 0
for i in range(width):
    start = (i, -1)
    dir = down
    energy = move(*start, *dir)
    distance = len(energy)
    if distance > max:
        max = distance

    start = (i, height)
    dir = up
    energy = move(*start, *dir)
    distance = len(energy)
    if distance > max:
        max = distance

for i in range(height):
    start = (-1, i)
    dir = right
    energy = move(*start, *dir)
    distance = len(energy)
    if distance > max:
        max = distance

    start = (width, i)
    dir = left
    energy = move(*start, *dir)
    distance = len(energy)
    if distance > max:
        max = distance 

print(max)
