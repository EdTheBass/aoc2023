test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

with open("day9.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def next_num(nodes):
    common_difference = [n - nodes[i] for i,n in enumerate(nodes[1:])]
    constant = len(list(dict.fromkeys(common_difference))) == 1
    if constant:
        return nodes[0] - common_difference[0]
    else:
        return nodes[0] - next_num(common_difference)

def extrapolated_sum(inp):
    predictions = []
    for line in inp:
        numbers = [int(_) for _ in line.strip().split(" ")]
        predictions.append(next_num(numbers))

    return sum(predictions)

# wtf why was day 9 so easy?? i only changed 3 indices and 2 signs
print(extrapolated_sum(puzzle_input))
