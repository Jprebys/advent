from itertools import combinations

layouts: list[str] = []
groups: list[list[int]] = []

with open("input.txt", "r") as f:
    for row in f:
        layout, group = row.split()
        layouts.append(layout)
        groups.append(list(map(int, group.split(","))))


def generate_bits(width, on_bits):
    result = []
    for bits in combinations(range(width), on_bits):
        s = ["."] * width
        for bit in bits:
            s[bit] = "#"
        result.append("".join(s))
    return result

def count_groups(layout):
    groups = []
    in_group = False
    this_group = 0

    for char in layout:
        if in_group:
            if char == "#":
                this_group += 1
            else:
                groups.append(this_group)
                in_group = False
                this_group = 0
        else:
            if char == "#":
                in_group = True
                this_group = 1

    if this_group:
        groups.append(this_group)
    return groups


total = 0
count = 0
for layout, group in zip(layouts, groups):
    this_total = 0
    missing_idx = [i for i, char in enumerate(layout) if char == "?"]
    missing = len(missing_idx)
    springs = layout.count("#")
    total_springs = sum(group)
    patterns = generate_bits(missing, total_springs - springs)
    for pattern in patterns:
        this_layout = list(layout)
        for char, idx in zip(pattern, missing_idx):
            this_layout[idx] = char
        if count_groups(this_layout) == group:
            this_total += 1

    count += 1
    total += this_total

print(total)