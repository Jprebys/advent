import copy
rules = {}
with open("input.txt") as f:
    rules_raw, _ = f.read().strip().split("\n\n")

    for line in rules_raw.splitlines():
        line = line.split("{")
        name = line[0]
        these = []
        for sub in line[1][:-1].split(","):
            sub = sub.split(":")
            if len(sub) == 1:
                these.append((sub[0],))
            else:
                pred, dest = sub
                attr, test, *val = pred
                val = int("".join(val))
                these.append((attr, test, val, dest))

        rules[name] = these

class Range:
    def __init__(self, xmin, xmax, mmin, mmax, amin, amax, smin, smax):
        self.xmin = xmin
        self.xmax = xmax
        self.mmin = mmin
        self.mmax = mmax
        self.amin = amin
        self.amax = amax
        self.smin = smin
        self.smax = smax

    def split(self, attr, test, val):
        passed = None
        failed = None
        maxval = getattr(self, f"{attr}max")
        minval = getattr(self, f"{attr}min")
        if test == ">":
            if minval > val:
                passed = copy.copy(self)
            if maxval <= val:
                failed = copy.copy(self)
            else:
                passmin = val + 1
                passmax = maxval
                failmin = minval
                failmax = val
                passed = copy.copy(self)
                failed = copy.copy(self)
                setattr(passed, f"{attr}min", passmin)
                setattr(passed, f"{attr}max", passmax)
                setattr(failed, f"{attr}min", failmin)
                setattr(failed, f"{attr}max", failmax)
        else: # test == "<"
            if maxval < val:
                passed = copy.copy(self)
            if minval >= val:
                failed = copy.copy(self)
            else:
                passmin = minval
                passmax = val - 1
                failmin = val
                failmax = maxval
                passed = copy.copy(self)
                failed = copy.copy(self)
                setattr(passed, f"{attr}min", passmin)
                setattr(passed, f"{attr}max", passmax)
                setattr(failed, f"{attr}min", failmin)
                setattr(failed, f"{attr}max", failmax)

        return passed, failed

    def score(self):
        return (self.xmax - self.xmin + 1) * (self.mmax - self.mmin + 1) * (self.amax - self.amin + 1) * (self.smax - self.smin + 1)

first_range = Range(1, 4000, 1, 4000, 1, 4000, 1, 4000)

total = 0
stack = [(first_range, "in", 0)]
while stack:
    range, ruleset, idx = stack.pop()
    rule = rules[ruleset][idx]
    if len(rule) == 1:
        rule = rule[0]
        if rule == "R":
            continue
        elif rule == "A":
            total += range.score()
            continue
        else:
            stack.append((range, rule, 0))
            continue
    else:
        attr, test, val, dest = rule
        passed, failed = range.split(attr, test, val)
        if passed is not None:
            if dest == "R":
                pass
            elif dest == "A":
                total += passed.score()
            else:
                stack.append((passed, dest, 0))
        if failed is not None:
            stack.append((failed, ruleset, idx+1))

print(total)