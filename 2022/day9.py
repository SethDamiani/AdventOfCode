with open("day9.txt") as f:
    data = f.readlines()

ddata = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2",
]

ddata = [
    "R 5",
    "U 8",
    "L 8",
    "D 3",
    "R 17",
    "D 10",
    "L 25",
    "U 20",
]

def diff(head, tail):
    vdist = abs(head[0]-tail[0])
    hdist = abs(head[1]-tail[1])
    return hdist, vdist

def move(head, tail):
    vdist = head[1]-tail[1]
    hdist = head[0]-tail[0]
    if vdist == 0 and hdist == 0:
        return 0, 0
    if hdist == 0:
        return 0, vdist//abs(vdist)
    if vdist == 0:
        return hdist//abs(hdist), 0
    vdist = vdist//abs(vdist)
    hdist = hdist//abs(hdist)
    return hdist, vdist

visited = set()
visited.add((0,0))
head = [0, 0]
tail = [0, 0]

for line in data:
    line = line.strip().split(" ")
    direction = line[0]
    distance = int(line[1])
    if direction == "R":
        head = [head[0]+distance, head[1]]
    elif direction == "L":
        head = [head[0]-distance, head[1]]
    elif direction == "D":
        head = [head[0], head[1]-distance]
    elif direction == "U":
        head = [head[0], head[1]+distance]
    
    while max(diff(head, tail)) > 1:
        m = move(head, tail)
        tail = [tail[0]+m[0], tail[1]+m[1]]
        visited.add((tail[0], tail[1]))
print(len(visited))

visited = set()
visited.add((0,0))
knots = []
for i in range(10):
    knots.append([0, 0])
for line in data:
    line = line.strip().split(" ")
    direction = line[0]
    distance = int(line[1])
    while distance > 0:
        head = knots[0]
        if direction == "R":
            head = [head[0]+1, head[1]]
        elif direction == "L":
            head = [head[0]-1, head[1]]
        elif direction == "D":
            head = [head[0], head[1]-1]
        elif direction == "U":
            head = [head[0], head[1]+1]
        knots[0] = head
        for i in range(1, len(knots)):
            head = knots[i-1]
            tail = knots[i]
            while max(diff(head, tail)) > 1:
                m = move(head, tail)
                tail = [tail[0]+m[0], tail[1]+m[1]]
                if i == len(knots)-1:
                    visited.add((tail[0], tail[1]))
            knots[i] = tail
        distance -= 1
print(len(visited))
