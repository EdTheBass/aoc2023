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

def bound(i,j,maxes):
    i_max,j_max = maxes
    return [min(max(0,i),i_max), min(max(0,j),j_max)]

def apply_shift(rc, shift, maxes):
    r,c = rc
    s_r,s_c = shift
    return bound(r+s_r,c+s_c,maxes)

def adjacents(rc, inp):
    r,c = rc
    char = inp[r][c]
    maxes = [len(inp)-1,len(inp[0])-1]
    
    if char == ".":
        return [],[]

    mapping = {"|": ([-1,0],[1,0]), "-": ([0,-1],[0,1]), "L": ([-1,0],[0,1]), "J": ([-1,0],[0,-1]), "7": ([1,0],[0,-1]), "F": ([1,0],[0,1])}
    try:
        shift1, shift2 = mapping.get(char)
        return apply_shift(rc, shift1, maxes), apply_shift(rc, shift2, maxes)
    except TypeError:
        # char is S so we need to find the adjacents of all the adjacents and see if any contain S
        possible_adjs = [[0,-1],[0,1],[-1,0],[1,0]]
        actual_adjs = []
        for a,b in possible_adjs:
            new_r, new_c = r+a, c+b
            if bound(new_r, new_c, maxes) == rc:
                continue

            if rc in adjacents([new_r,new_c],inp):
                actual_adjs.append([new_r, new_c])
        return actual_adjs

def traverse(start, inp):
    curr,_ = adjacents(start,inp)
    path = [start,curr]
    while True:
        children = adjacents(curr,inp)
        new_children = [c for c in children if c not in path]
        if new_children:
            curr = new_children[0]
        else:
            break
        path.append(curr)

    return len(path)

def longest_path(inp):
    global height,max_height
    # [row, column]
    start = []
    for i,l in enumerate(inp):
        if "S" in l:
            start = [i, l.index("S")]
            break
    
    p_length = traverse(start,inp)

    return p_length//2

print(longest_path(puzzle_input))
