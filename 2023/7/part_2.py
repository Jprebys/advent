import collections

card_map = {str(l): l for l in range(2, 10)}
card_map.update({"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14})
class Hand:
    def __init__(self, cards, bid, ocards):
        self.cards = cards
        self.bid = int(bid)
        self.ocards = ocards

        counts = list(dict(collections.Counter(cards)).values())
        counts.sort(reverse=True)
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




def replace_jokers(cards: list):
    if 1 not in cards:
        return [cards]
    
    index = cards.index(1)
    sets = []
    for i in range(2, 15):
        new_set = [c for c in cards]
        new_set[index] = i
        sets.extend(replace_jokers(new_set))
    
    return sets



            
hand_types = ["card", "two", "pairs", "three", "house", "four", "five"]

hands = []
with open("input.txt", "r") as f:
    for line in f:
        cards, bid = line.split()
        cards = list(map(card_map.get, cards))
        ocards = cards
        if 1 not in cards:
            hands.append(Hand(cards, bid, ocards))
        else:

            cards = replace_jokers(cards)
            this_set = []
            for card in cards:
                this_set.append(Hand(card, bid, ocards))
            for typ in reversed(hand_types):

                hits = [card for card in this_set if card.type == typ]

                if hits:
                    hits.sort(key=lambda x: x.cards, reverse=True)
                    hands.append(hits[0])
                    break
        # print(line, hands[-1].cards)
        # input()

    

total = 0
mult = 1
for typ in hand_types:
    for hand in sorted([h for h in hands if h.type == typ], key=lambda x: x.ocards):
        print(hand.cards)
        total += mult * hand.bid
        mult += 1
print(len(hands))

print(total)