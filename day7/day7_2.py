import re

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()

with open("day7.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def get_val(card):
    return int(card) if card.isnumeric() else {"J":1,"T":10,"Q":11,"K":12,"A":13}.get(card)

def choose_wildcard(hand, counts):
    try:
        wildcard_card = sorted([[l, counts[i], get_val(l)] for i,l in enumerate(hand) if l != "J"], key=lambda x: (x[1],x[2]), reverse=True)[0][0]
    except IndexError:
        wildcard_card = "A"
    if wildcard_card == "J": print(hand)
    return wildcard_card

def value(hand, wildcard=False):
    ranks = {(1,1,1,1,1): 1, (1,1,1,2): 2, (1,2,2): 3, (1,1,3): 4, (2,3): 5, (1,4): 6, (5,): 7}
    values = [get_val(c) for c in hand]
    unique_cards = list(dict.fromkeys(hand))
    unsorted_counts = [hand.count(a) for a in unique_cards]
    
    if not wildcard:
        wildcard = choose_wildcard(unique_cards, unsorted_counts)
        replaced_hand = hand.replace("J", wildcard)
        hand_type,_ = value(replaced_hand, wildcard=True)
    else:
        counts = tuple(sorted(unsorted_counts))
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
