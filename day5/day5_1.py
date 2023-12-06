import re

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

with open("day5.txt", "r") as puzzle_input_file:
    puzzle_input = puzzle_input_file.read()

def parse_map_matches(maps):
    source = maps[0]
    destination = maps[1]
    numbers = [[int(m) for m in n] for n in re.findall(r"^(\d+) (\d+) (\d+)", maps[2], re.MULTILINE)]
    src_nums = [n[1] for n in numbers]
    dest_nums = [n[0] for n in numbers]
    ranges = [n[2] for n in numbers]

    def map_func(x):
        for i,s in enumerate(src_nums):
            if s <= x < s+ranges[i]:
                return x + (dest_nums[i] - s)
        return x

    return source, destination, map_func

def find_smallest_loc(seeds, maps):
    smallest_loc = 1e100
    for s in seeds:
        curr_num = s
        for m in maps:
            map_func = m[2]
            curr_num = map_func(curr_num)
        smallest_loc = curr_num if curr_num < smallest_loc else smallest_loc
    return smallest_loc

def location_num(inp):
    seeds = [int(n) for n in re.match(r"seeds: (.*)", inp).group(1).split(" ")]
    map_matches = re.findall(r"(^.*)-to-(.*?) map:\n([^a-z]*)", inp, re.MULTILINE)
    maps = []
    for m in map_matches:
        src, dest, m_func = parse_map_matches(m)
        maps.append((src, dest, m_func))

    return find_smallest_loc(seeds, maps)

print(location_num(puzzle_input))
