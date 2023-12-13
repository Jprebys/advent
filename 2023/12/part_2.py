layouts: list[str] = []
groups: list[list[int]] = []

from functools import lru_cache

with open("input.txt", "r") as f:
    for row in f:
        layout, group = row.split()
        layout = [layout] * 5
        layout = "?".join(layout)
        
        layouts.append(layout)
        
        group = [group] * 5
        group = ",".join(group)
        groups.append(tuple(map(int, group.split(","))))

def validate(real, proposed):
    for r, p in zip(real, proposed):
        if r == "#" and p != "#":
            return False
        if r == "." and p == "#":
            return False
    return True

def make_part(index, length, size):
    this_part = ["."] * size
    for j in range(index, index+length):
        this_part[j] = "#"
    return this_part

@lru_cache(maxsize=None)
def count_possibilities(layout: str, group: tuple[int], level):
    if not group:
        return 0 if layout.count("#") > 0 else 1
    else:
        total = 0
        total_space = len(layout) - (sum(group[1:]) + len(group[1:]))
        for i in range(total_space - group[0] + 1):
            this_part = make_part(i, group[0], group[0] + i + 1)
            if validate(layout, this_part):
                start = i + group[0] + 1
                total += count_possibilities(layout[start:], group[1:], level + len(this_part))
        return total

total = 0
n_layouts = len(layouts)
for i, (layout, group) in enumerate(zip(layouts, groups)):
    possibilities = count_possibilities(layout, group, 0)
    print(f"{i+1}/{n_layouts}:", possibilities)
    total += possibilities
print(total)