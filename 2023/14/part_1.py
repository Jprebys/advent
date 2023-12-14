with open("input.txt", "r") as f:
    lines = f.read().splitlines()

width = len(lines[0])
height = len(lines)

total = 0
for x in range(width):
    base = 0
    for y, line in enumerate(lines):
        if line[x] == "O":
            total += (height - base)
            print(total)
            base += 1
        elif line[x] == "#":
            base = y+1
        
print(total)


