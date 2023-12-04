games = []

mins = {
    "red": 0,
    "green": 0,
    "blue": 0
}

total = 0
with open("input.txt", "r") as f:
    for i, game in enumerate(f, start=1):
        data = game.split(": ")[1]
        mins = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in data.split("; "):

            for section in round.split(", "):
                number, color = section.split()
                number = int(number)
                if number > mins[color]:
                    mins[color] = number

        rapid = 1
        for number in mins.values():
            rapid *= number
        total += rapid

print(rapid)




print(total)
