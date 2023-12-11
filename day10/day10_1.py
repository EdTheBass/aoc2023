import re

test_input1 = """.....
.S-7.
.|.|.
.L-J.
.....""".splitlines()

test_input2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ""".splitlines()

with open("day10.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def apply_shift(rc, shift, maxes):
    r,c = rc
    s_r,s_c = shift
    return [min(max(0,r+s_r),maxes[0]), min(max(0,c+s_c),maxes[1])]

def adjacents(rc, inp):
    r,c = rc
    char = inp[r][c]
    maxes = [len(inp)-1,len(inp[0])-1]
    
    mapping = {"|": ([-1,0],[1,0]), "-": ([0,-1],[0,1]), "L": ([-1,0],[0,1]), "J": ([-1,0],[0,-1]), "7": ([1,0],[0,-1]), "F": ([1,0],[0,1]), ".": []}
    try:
        shift1, shift2 = mapping.get(char)
        return apply_shift(rc, shift1, maxes), apply_shift(rc, shift2, maxes)
    except TypeError:
        # char is S so we need to find the adjacents of all the adjacents and see if any contain S
        possible_adjs = [[]]


def longest_path(inp):
    # [row, column]
    start = []
    for i,l in enumerate(inp):
        if "S" in l:
            start = [i, l.index("S")]
            break

    print(start)
    print(adjacents(start, inp))

    return 0

print(longest_path(test_input1))
# print(longest_path(test_input2))
