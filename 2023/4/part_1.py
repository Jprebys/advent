
total = 0

with open("input.txt", "r") as f:
    for line in f:
        
        winners = line[line.index(":") + 2: line.index("|") - 1].split()
        cards = line[line.index("|") + 2:].split()

        points = 0
        for card in cards:
            if card in winners:
                if not points:
                    points = 1
                else:
                    points *= 2
        total += points

print(total)
        
