
games = {}
with open("input.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        
        winners = line[line.index(":") + 2: line.index("|") - 1].split()
        cards = line[line.index("|") + 2:].split()
        games[i] = winners, cards


def count_matches(game):
    matches = 0
    winners, cards =  game
    for card in cards:
        if card in winners:
            matches += 1
    return matches

counts = {i: 1 for i in games}

for i, count in counts.items():
    print(f"{i}/{len(counts)}", count)
    for j in range(1, count_matches(games[i]) + 1):
        counts[i + j] += 1 * count

print(sum(counts.values()))

        
