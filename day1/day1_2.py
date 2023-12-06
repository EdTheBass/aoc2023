import re

test_input = """two1nine
eighthree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

with open("day1.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.readlines()

def find_numbers(line):
    num_match = {"one": 1,"two": 2, "three": 3, "four": 4, "five": 5,
                 "six": 6, "seven": 7, "eight": 8, "nine": 9,
                 "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                 "6": 6, "7": 7, "8": 8, "9": 9}
    first_digit = re.match(r"^.*?(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line).group(1)
    last_digit = re.match(r"^.*(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line).group(1)
    first = num_match.get(first_digit)
    last = num_match.get(last_digit)
    return first*10 + last

def find_calibration(inp):
    total = 0
    for line in inp:
        num = find_numbers(line.strip())
        total += num

    return total

print(find_calibration(puzzle_input))