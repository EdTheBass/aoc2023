import re

test_input1 = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........""".splitlines()

test_input2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".splitlines()

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

    return path

def longest_path(inp):
    global height,max_height
    # [row, column]
    start = []
    for i,l in enumerate(inp):
        if "S" in l:
            start = [i, l.index("S")]
            break
    
    path = traverse(start, inp)
    for i in range(len(inp)): 
        for j in range(len(inp[0])): 
            if [i,j] not in path: 
                inp[i] = inp[i][:j] + "." + inp[i][j+1:]
    
    

    return 1

print(longest_path(test_input2))
