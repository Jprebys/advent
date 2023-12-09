lines = []
with open("input.txt", "r") as f:
    for line in f:
        lines.append(list(map(int, line.strip().split())))


total = 0
for line in lines:
    sets = [line]
    while any(sets[-1]):
        sets.append([sets[-1][i+1] - sets[-1][i] for i in range(len(sets[-1])-1)])
    last = 0
    for s in reversed(sets):
        last = s[0] - last
    total += last
print(total)