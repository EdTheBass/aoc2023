import re
import numpy as np

test_input = """Time:      7  15   30
Distance:  9  40  200"""

with open("day6.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.read()

def find_options(time, dist):
    winning_times = 0
    t1,t2 = sorted(np.roots([1, -time, dist]))
    winning_times = np.floor(t2) - np.floor(t1)
    return int(winning_times)


def combinations(inp):
    time = int(re.sub(r" +", "", re.search(r"Time:[ ]*(\d.*)\n", inp).group(1)))
    dist = int(re.sub(r" +", "", re.search(r"Distance:[ ]*(\d.*)", inp, re.MULTILINE).group(1)))

    return find_options(time, dist)

# me when this problem is literally a quadratic
print(combinations(puzzle_input))
