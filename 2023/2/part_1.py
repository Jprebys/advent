games = []

maxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0
with open("input.txt", "r") as f:
    for i, game in enumerate(f, start=1):
        data = game.split(": ")[1]
        possible = True
        for round in data.split("; "):
            round_possible = True
            for section in round.split(", "):
                number, color = section.split()
                number = int(number)
                round_possible = round_possible and number <= maxes[color]

            possible = possible and round_possible
        if possible:
            print(game)
            total += i





print(total)
