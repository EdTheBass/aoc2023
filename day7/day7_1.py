import re

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()

with open("day7.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def value(hand):
    # rank: 
    card_vals = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    ranks = {(1,1,1,1,1): 1, (1,1,1,2): 2, (1,2,2): 3, (1,1,3): 4, (2,3): 5, (1,4): 6, (5,): 7}
    get_val = lambda card: int(card) if card.isnumeric() else card_vals.get(card)
    values = [get_val(c) for c in hand]
    counts = tuple(sorted([hand.count(a) for a in list(dict.fromkeys(hand))]))
    hand_type = ranks.get(counts)
     
    return hand_type, values

def total_winnings(inp):
    hand_data = []
    for l in inp:
        l = l.strip()
        hand = re.match("(.*) ", l).group(1)
        bet = int(re.search(" (\d+)", l).group(1))
        
        h_type, c_vals = value(hand)

        # [bet, h_type, c1, c2, c3, c4, c5]
        hand_data.append([bet, h_type] + [v for v in c_vals])
        
    key = lambda x: tuple([x[i] for i in range(1,7)])
    
    ranked_bets = sorted(hand_data, key=key)
    winnings = sum([h[0]*(i+1) for i,h in enumerate(ranked_bets)])

    return winnings

print(total_winnings(puzzle_input))
