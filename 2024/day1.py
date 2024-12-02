with open("day1.txt") as f:
    lists = f.readlines()
    left = []
    right = []
    for line in lists:
        s = line.split(" ")
        left.append(int(s[0]))
        right.append(int(s[-1]))
    left.sort()
    right.sort()
    part1 = 0
    for i in range(len(left)):
        part1 += abs(left[i] - right[i])
    print(f"Part 1: {part1}")
    part2 = 0
    for i in range(len(left)):
        part2 += left[i] * right.count(left[i])
    print(f"Part 2: {part2}")
