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

    u_stars = re.finditer(r"\*", up)
    l_star = l_i if "*" in left else -1
    r_star = r_i if "*" in right else -1
    d_stars = re.finditer(r"\*", down)
    total_stars = []
    for _ in u_stars:
        s = _.span()[0]
        total_stars.append(tuple([line-1, l_i+s]))
    if l_star != -1:
        total_stars.append(tuple([line, l_star]))
    if r_star != -1:
        total_stars.append(tuple([line, r_star]))
    for _ in d_stars:
        s = _.span()[0]
        total_stars.append(tuple([line+1, l_i+s]))
    return total_stars


def find_part_nums(inp):
    total = 0
    asterisks = {}
    for i,line in enumerate(inp):
        numbers = re.finditer(r"\d+", line)
        for n in numbers:
            l,r = n.span()
            n_match = n.group(0)
            a_s = find_asterisk(inp, i, l, r)
            for _ in a_s:
                if not asterisks.get(_): asterisks.update({_:[n_match]}) 
                else: asterisks[_].append(n_match)

    vals = asterisks.values()
    for v in vals:
        if len(v) == 2:
            gear_num = int(v[0]) * int(v[1])
            total += gear_num
    
    return total

# fuck this puzzle
print(find_part_nums(puzzle_input))