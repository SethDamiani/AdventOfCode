text = [l.strip() for l in open("2023/day12e.txt").readlines()]

def valid(pattern, key):
    check = pattern.split(".")
    check = [len(c) for c in check if len(c) > 0]
    return check == key

part1 = 0
for line in text:
    print(line, end="\t\t")
    pattern, key = line.split(" ")
    key = [int(i) for i in key.split(",")]
    # find all possible arrangements
    total = pattern.count("#")
    ct = 0
    for i in range(total):
        maskstr = ("1"*total)
        mask = int(maskstr, 2)
        #print(mask)
        curr = ""
        for j in range(len(pattern)):
            if pattern[j] == ".":
                curr += "."
            elif pattern[j] == "#":
                curr += "#"
            else:
                c = bin(mask).split("b")[1][-1]
                if c == "1":
                    curr += "#"
                else:
                    curr += "."
                mask -= 1
        print(f"\n\tchecking {curr} to {key}", end="")
        if valid(curr, key):
            ct += 1
    print(ct)
    part1 += ct

print(part1)
