import re

test_input1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".splitlines()

test_input2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".splitlines()

with open("day8.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def parse_line(line):
    line = re.sub(r" ", "", line).strip()
    node = re.search(r"([A-Z]{3}).*([A-Z]{3}).*([A-Z]{3})", line)
    element, left, right = node.group(1), node.group(2), node.group(3)
    return element, left, right

def steps_required(inp):
    instructions = [int(n) for n in re.search("([LR]+)", inp[0]).group(1).replace("L","0").replace("R","1")]
    elements = []
    pairs = []

    for line in inp[2:]:
        e, l, r = parse_line(line)
        elements.append(e)
        pairs.append([l,r])

    i = elements.index("AAA")
    steps = 0
    while elements[i] != "ZZZ":
        instruct = instructions[steps%len(instructions)]
        i = elements.index(pairs[i][instruct])
    
        steps += 1
        
    return steps


print(steps_required(puzzle_input))

