import collections

class Number:
    def __init__(self, value, x, y):
        self.value = value
        self.digits = len(str(value))
        self.x = x
        self.y = y


with open("input.txt", "r") as f:
    board = [line.strip() for line in f]

width = len(board[0])
height = len(board)

numbers = []

for y in range(height):
    x = 0
    while x < width:
        digits = ""
        start_x = x
        while board[y][x].isdigit():
            digits += board[y][x]
            x += 1
            if x == width:
                break
        if digits:
            numbers.append(Number(int(digits), start_x, y))
        
        x += 1
        
def check_for_gear(board, width, height, x, y):
    if x < 0 or y < 0 or x >= width or y >= height:
        return False
    return board[y][x] == "*"

total = 0

gears = collections.defaultdict(list)
for num in numbers:
    print(num.value, num.digits, num.x, num.y)
    surrounding = []
    surrounding.append((num.x - 1, num.y))
    surrounding.append((num.x + num.digits, num.y))

    for x in range(num.digits + 2):
        surrounding.append((num.x + x - 1, num.y - 1))
        surrounding.append((num.x + x - 1, num.y + 1))

    for x, y in surrounding:
        if check_for_gear(board, width, height, x, y):
            gears[(x, y)].append((num.value))


total = 0
for ratios in gears.values():
    if len(ratios) == 2:
        total += ratios[0] * ratios[1]

print(total)


    
