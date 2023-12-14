import numpy as np 

with open("input.txt", "r") as f:
    txt = f.read()
    lines = [list(x) for x in txt.splitlines()]

array = np.array(lines)

def drop(array: np.ndarray):
    for x in range(array.shape[1]):
        base = 0
        for y in range(array.shape[0]):
            if array[y, x] == "#":
                base = y + 1
            if array[y, x] == "O":
                array[y, x], array[base, x] = array[base, x], array[y, x]
                base += 1
    return array

def cycle(array: np.ndarray):
    for _ in range(4):
        array = drop(array)
        array = np.rot90(array, k=-1)
    return array 

answers = []
arrays = []
for i in range(1_000_000_000):
    array = cycle(array)
    if array.tobytes() in answers:
        cycle_start = answers.index(array.tobytes())
        cycle_len = i - cycle_start
        break
    answers.append(array.tobytes())
    arrays.append(array.copy())

idx = ((999999999 - cycle_start) % cycle_len) + cycle_start
end = arrays[idx]

def score(array):
    total = 0
    height = array.shape[0]
    for x in range(array.shape[1]):
        for y in range(array.shape[0]):
            if array[y, x] == "O":
                total += (height - y)
    return total

print(score(end))





    

