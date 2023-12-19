
with open("input.txt", "r") as f:
    codes = f.read().strip().split(",")

def hashit(code):
    sub = 0
    for c in code:
        sub += ord(c)
        sub *= 17
        sub &= 255
    return sub

boxes = []
focals = []
for i in range(256):
    boxes.append([])
    focals.append([])

for code in codes:
    if code[-1] == "-":
        label = code[:-1]
        hsh = hashit(label)
        if label in boxes[hsh]:
            idx = boxes[hsh].index(label)
            del boxes[hsh][idx]
            del focals[hsh][idx]
    else:
        label, length = code.split("=")
        hsh = hashit(label)
        if label in boxes[hsh]:
            idx = boxes[hsh].index(label)
            focals[hsh][idx] = int(length)
        else:
            boxes[hsh].append(label)
            focals[hsh].append(int(length))

total = 0
for i, box in enumerate(focals, start=1):
    for j, slot in enumerate(box, start=1):
        total += i * j * slot

print(total)
