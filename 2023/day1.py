sample = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

m = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

def sub(string, substring):
    if substring in string:
        return string.index(substring)
    return -1

def subr(string, substring):
    if substring in string:
        return string.rindex(substring)
    return -1

def transform(string):
    priorities = [
        sub(string, "one"),
        sub(string, "two"),
        sub(string, "three"),
        sub(string, "four"),
        sub(string, "five"),
        sub(string, "six"),
        sub(string, "seven"),
        sub(string, "eight"),
        sub(string, "nine"),
    ]
    prioritiesr = [
        subr(string, "one"),
        subr(string, "two"),
        subr(string, "three"),
        subr(string, "four"),
        subr(string, "five"),
        subr(string, "six"),
        subr(string, "seven"),
        subr(string, "eight"),
        subr(string, "nine"),
    ]
    reploc = [p for p in priorities if p != -1]
    if reploc:
        rep = priorities.index(min(reploc))
        string = string.replace(m[rep], str(rep+1))
    reploc2 = [p for p in prioritiesr if p != -1]
    if reploc2:
        rep2 = prioritiesr.index(max(reploc2))
        string = string.replace(m[rep2], str(rep2+1))
    return string

with open("day1.txt") as f:
    text = f.readlines()
    #text = sample
    total = 0
    total2 = 0
    for line in text:
        line = line.strip()
        line1 = [c for c in line if c.isdigit()]
        #ns = line1[0]+line1[-1]
        #total += int(ns)
        line2 = transform(line)
        line2 = [c for c in line2 if c.isdigit()]
        ns = line2[0]+line2[-1]
        print(line, ns)
        total2 += int(ns)
print(f"part 1: {total}")
print(f"part 2: {total2}")