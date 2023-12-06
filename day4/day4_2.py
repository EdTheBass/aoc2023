import re

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()


with open("day4.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def points(line):
    matches = 0
    card_num = int(re.search(r"Card *(\d+)", line).group(1))
    winning_nums = list(dict.fromkeys([int(n) for n in re.findall(r"(\d+(?=.*\|)(?!.*:))", line)]))
    my_numbers = list(dict.fromkeys([int(n) for n in re.findall(r"(\d+(?!.*\|))", line)]))
    
    for num in my_numbers:
        if num in winning_nums:
            matches += 1
    
    return matches+1 if matches else 


def total_points(inp):
    total = 0
    for l in inp:
        num = points(l.strip())
        print(num)
        total += num

    return total


print(total_points(puzzle_input))
