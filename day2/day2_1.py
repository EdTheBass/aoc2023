import re

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".splitlines()

with open("day2.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def find_numbers(line):
    maximums = {"red": 12, "green": 13, "blue": 14}
    line = re.sub(r" ", "", line, 0)
    game_id = int(re.match(r"(?:Game)(\d+)", line).group(1))
    ball_nums = re.findall(r"(\d+[^:;\n,\d]+)", line)
    for n in ball_nums:
        num, col = int(re.match(r"(\d+)", n).group(1)), re.search(r"([a-z]+)", n).group(1)
        if num > maximums.get(col):
            return 0
    return game_id

def find_ids(inp):
    total = 0
    for line in inp:
        num = find_numbers(line.strip())
        total += num
    
    return total

print(find_ids(puzzle_input))