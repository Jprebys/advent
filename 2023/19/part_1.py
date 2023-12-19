
from collections import namedtuple
from functools import partial

Part = namedtuple("Part", ["x", "m", "a", "s"])

def greater(val, a, p):
    return getattr(p, a) > val

def lesser(val, a, p):
    return getattr(p, a) < val

rules = {}
parts = []
with open("input.txt") as f:
    rules_raw, parts_raw = f.read().strip().split("\n\n")

    for line in rules_raw.splitlines():
        line = line.split("{")
        name = line[0]
        these = []
        for sub in line[1][:-1].split(","):
            sub = sub.split(":")
            if len(sub) == 1:
                these.append(((lambda *_: True), sub[0]))
            else:
                pred, dest = sub
                attr, test, *val = pred
                val = int("".join(val))
                if test == "<":
                    these.append((partial(lesser, val, attr), dest))
                elif test == ">":
                    these.append((partial(greater, val, attr), dest))
                else:
                    raise ValueError(f"unrecognized test {test}")

        rules[name] = these

    for raw in parts_raw.splitlines():
        components = []
        for attr in raw[1:-1].split(","):
            components.append(int(attr[2:]))
        parts.append(Part(*components))

def test_part(part):
    ruleset = rules["in"]
    rule_idx = 0
    while True:
        cond, dest = ruleset[rule_idx]
        if cond(part):
            if dest == "A":
                return True
            if dest == "R":
                return False
            ruleset = rules[dest]
            rule_idx = 0
        else:
            rule_idx += 1


total = 0
for part in parts:
    if test_part(part):
        total += sum(part)

print(total)

# print(sum(sum(part) for part in parts if test_part(part)))




        


