totals = [0]
with open("day1.txt") as f:
    for l in f:
        if l == "\n":
            totals.append(0)
        else:
            totals[-1] += int(l)
totals.sort()
print(f"Part 1: {totals[-1]} ")
print(f"Part 2: {totals[-1]+totals[-2]+totals[-3]}")
