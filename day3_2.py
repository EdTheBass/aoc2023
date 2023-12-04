import re

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()

with open("day3.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def find_asterisk(inp, line, l, r):
    line_text = inp[line]
    l_i = max(0, l-1)
    r_i = min(len(line_text)-1, r)
    u_i = max(0, line-1)
    d_i = min(len(inp)-1, line+1)

    up = inp[u_i][l_i:r_i+1]
    left = line_text[l_i]
    right = line_text[r_i]
    down = inp[d_i][l_i:r_i+1]

    if "*" in up:
        return u_i, l+up.index("*")-1
    if "*" in left:
        return line, l-1
    if "*" in right:
        return line, 

def find_part_nums(inp):
    total = 0
    for i,line in enumerate(inp):
        numbers = re.finditer(r"\d+", line)
        for n in numbers:
            l,r = n.span()
            adjacents = find_adjacents(inp, i, l, r)
            if re.search(r"[^\d.\n]", adjacents) is not None:
                total += int(n.group())
    return total

print(find_part_nums(puzzle_input),)
