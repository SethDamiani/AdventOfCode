text = [l.strip() for l in open("2023/day9.txt").readlines()]

part1 = 0
for line in text:
    m = [[int(x) for x in line.split(" ")]]
    while m[-1].count(0) != len(m[-1]):
        m.append([])
        for i in range(1, len(m[-2])):
            m[-1].append(m[-2][i] - m[-2][i-1])
    for i in range(-1, -1*(len(m)+1), -1):
        if i == -1:
            m[i].append(0)
            continue
        m[i].append(m[i][-1] + m[i+1][-1])
    part1 += m[0][-1]
print(part1)

part2 = 0
for line in text:
    m = [[int(x) for x in line.split(" ")[::-1]]]
    while m[-1].count(0) != len(m[-1]):
        m.append([])
        for i in range(1, len(m[-2])):
            m[-1].append(m[-2][i] - m[-2][i-1])
    for n in m:
        print(n)
    for i in range(-1, -1*(len(m)+1), -1):
        if i == -1:
            m[i].append(0)
            continue
        m[i].append(m[i][-1] + m[i+1][-1])
    part2 += m[0][-1]
    print()
    for n in m:
        print(n)
    print("\n\n")
print(part2)
