import re

test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

with open("day1.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def find_numbers(line):
    first_digit = re.findall(r"^[a-zA-Z]*(\d)", line)[0]
    last_digit = re.findall(r"(\d)[a-zA-Z]*$", line)[0]
    return int(first_digit)*10 + int(last_digit)

def find_calibration(inp):
    total = 0
    for line in inp:
        num = find_numbers(line.strip())
        total += num

    return total

print(find_calibration(puzzle_input))