with open("day4.txt") as f:
    data = f.readlines()
ddata = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8"
]

pairs = []

for line in data:
    one, two = line.split(",")
    one = [int(x) for x in one.split("-")]
    two = [int(x) for x in two.split("-")]
    pairs.append([one, two])

# part 1
count = 0
for pair in pairs:
    if (pair[0][0] <= pair[1][0] and pair[1][1] <= pair[0][1]) or (pair[1][0] <= pair[0][0] and pair[0][1] <= pair[1][1]):
        count += 1
print(count)

# part 2
count = 0
for pair in pairs:
    res = set(range(pair[0][0], pair[0][1]+1)).intersection(range(pair[1][0], pair[1][1]+1))
    if len(res) > 0:
        count += 1
print(count)
