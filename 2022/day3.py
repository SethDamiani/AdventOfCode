with open("day3.txt") as f:
    ff = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]
    total = 0
    for line in f:
        line = line.strip()
        one = line[:len(line)//2]
        two = line[len(line)//2:]
        for c in one:
            if c in two:
                char = c
                break
        o = ord(char)
        if o >= 97:
            o -= 96
        else:
            o -= 64
            o += 26
        #print(f"{c}: {o}")
        total += o
    print(f"Part 1: {total}")
data = None
with open("day3.txt") as f:
    data = f.readlines()
total = 0
for i in range(0, len(data), 3):
    one = data[i].strip()
    two = data[i+1].strip()
    three = data[i+2].strip()
    for c in one:
        if c in two and c in three:
            char = c
            break
    o = ord(char)
    if o >= 97:
        o -= 96
    else:
        o -= 64
        o += 26
    total += o
print(f"Part 2: {total}")