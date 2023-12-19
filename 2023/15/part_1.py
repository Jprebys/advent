
with open("input.txt", "r") as f:
    codes = f.read().strip().split(",")

def hashit(code):
    sub = 0
    for c in code:
        sub += ord(c)
        sub *= 17
        sub &= 255
    return sub

print(sum(hashit(code) for code in codes))
