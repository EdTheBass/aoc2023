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

def get_seeds(seeds_range):
    s = []
    for i in range(0,len(seeds_range),2):
        start = seeds_range[i]
        end = start + seeds_range[i+1]
        s.append(range(start, end))
        print(f"Seeds: {100*(i+2)/len(seeds_range):0.2f}%")
    return s

def parse_map_matches(maps):
    destination = maps[0]
    source = maps[1]
    numbers = [[int(m) for m in n] for n in re.findall(r"^(\d+) (\d+) (\d+)", maps[2], re.MULTILINE)]
    src_nums = [n[1] for n in numbers]
    dest_nums = [n[0] for n in numbers]
    ranges = [n[2] for n in numbers]

    def map_func(x):
        for i,d in enumerate(dest_nums):
            if d <= x < d+ranges[i]:
                return x - d + src_nums[i]
        return x

    return source, destination, map_func

def find_smallest_loc(seeds, maps):
    def is_in_seeds(n):
        for r in seeds:
            if n in r: return True
        return False
    
    l = 1
    while True:
        if l % 100 == 0: print(f"Location: {l}")
        curr_num = l
        for m in maps[::-1]:
            map_func = m[2]
            curr_num = map_func(curr_num)

        if is_in_seeds(curr_num):
            return l

        l += 1

def location_num(inp):
    seeds_range = [int(n) for n in re.match(r"seeds: (.*)", inp).group(1).split(" ")]
    seeds = get_seeds(seeds_range)
    map_matches = re.findall(r"(^.*)-to-(.*?) map:\n([^a-z]*)", inp, re.MULTILINE)
    maps = []
    for m in map_matches:
        # inverse map matches to find seed numbers
        src, dest, m_func = parse_map_matches(m)
        maps.append((src, dest, m_func))

    return find_smallest_loc(seeds, maps)

# best AoC puzzle so far 100%
print(location_num(puzzle_input))
