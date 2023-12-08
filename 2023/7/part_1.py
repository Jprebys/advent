import collections

card_map = {str(l): l for l in range(2, 10)}
card_map.update({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14})
class Hand:
    def __init__(self, cards, bid):
        self.cards = list(map(card_map.get, cards))
        self.bid = int(bid)

        counts = sorted(list(dict(collections.Counter(self.cards)).values()), reverse=True)
        f = counts[0]
        if f == 5:
            self.type = "five"
        elif f == 4:
            self.type = "four"
        elif f == 3:
            if counts[1] == 2:
                self.type = "house"
            else:
                self.type = "three"
        elif f == 2:
            if counts[1] == 2:
                self.type = "pairs"
            else:
                self.type = "two"
        else:
            self.type = "card"



hands = []
with open("input.txt", "r") as f:
    for line in f:
        hands.append(Hand(*line.split()))


hand_types = ["card", "two", "pairs", "three", "house", "four", "five"]
total = 0
mult = 1
for typ in hand_types:
    for hand in sorted([h for h in hands if h.type == typ], key=lambda x: x.cards):
        total += mult * hand.bid
        mult += 1
print(total)