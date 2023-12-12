from math import sqrt, floor, ceil


text = [l.strip() for l in open("2023/day6.txt").readlines()]
text = [l.split(":")[1].strip() for l in text]
times, dists = [[int(n) for n in l.split(" ") if len(n) > 0] for l in text]
print(times)
print(dists)

def quadratic_formula(a, b, c) -> tuple[int,int]:
    x1 = ((-1*b) + sqrt(b**2 - (4*a*c))) / (2*a)
    x2 = ((-1*b) - sqrt(b**2 - (4*a*c))) / (2*a)
    return ceil(min(x1, x2)), floor(max(x1, x2))

part1 = 1
for i in range(len(times)):
    # y = (9-x)*x
    a = -1
    b = times[i]
    c = -(dists[i]+.5)
    x1, x2 = quadratic_formula(a, b, c)
    possibilities = abs(x1-x2)+1
    part1 *= possibilities
print(f"Part 1: {part1}")

a = -1
b = int("".join([str(t) for t in times]))
c = -(float("".join([str(d) for d in dists])))
x1, x2 = quadratic_formula(a, b, c)
possibilities = abs(x1-x2)+1
print(f"Part 2: {possibilities}")
