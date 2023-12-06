import re

test_input = """Time:      7  15   30
Distance:  9  40  200"""

with open("day6.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.read()

def find_options(time, dist):
    winning_times = 0
    for t in range(1,1+time//2):
        distance = t * (time - t)
        if distance > dist:
            winning_times += 1
    return winning_times


def combinations(inp):
    time = int(re.sub(r" +", "", re.search(r"Time:[ ]*(\d.*)\n", inp).group(1)))
    dist = int(re.sub(r" +", "", re.search(r"Distance:[ ]*(\d.*)", inp, re.MULTILINE).group(1)))

    total = 2 * find_options(time, dist)-1

    return total

# takes ages ngl
print(combinations(puzzle_input))
