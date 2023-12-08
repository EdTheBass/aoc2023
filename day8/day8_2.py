import re

test_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".splitlines()


with open("day8.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def gcd(a, b):
    smaller, larger = min(a, b), max(a, b)
    result = larger - smaller
    while result >= smaller:
        result -= smaller

    if result == 0:
        return smaller
            
    return gcd(smaller, result)

def lcm(a, b):
    return a*b // gcd(a,b)

def parse_line(line):
    line = re.sub(r" ", "", line).strip()
    node = re.search(r"([A-Z0-9]{3}).*([A-Z0-9]{3}).*([A-Z0-9]{3})", line)
    element, left, right = node.group(1), node.group(2), node.group(3)
    return element, left, right

def steps_required(inp):
    instructions = [int(n) for n in re.search("([LR]+)", inp[0]).group(1).replace("L","0").replace("R","1")]
    elements = []
    pairs = []
    starts = []

    for i,line in enumerate(inp[2:]):
        e, l, r = parse_line(line)
        if e.endswith("A"):
            starts.append(i)
        elements.append(e)
        pairs.append([l,r])

    each_step = []
    for s in starts:
        steps = 0
        i = s
        while not elements[i].endswith("Z"):
            instruct = instructions[steps%len(instructions)]
            i = elements.index(pairs[i][instruct])
        
            steps += 1

        each_step.append(steps)
        
    total_steps = 1
    for s in each_step:
        total_steps = lcm(s,total_steps)
    
    return total_steps

print(steps_required(puzzle_input))
