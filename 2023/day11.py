text = [l.strip() for l in open("2023/day11.txt").readlines()]
HEIGHT = len(text)
WIDTH = len(text[0])

def expand_universe(expand_by: int):
    global ROWS, COLS
    COLS = []
    for x in range(WIDTH):
        current_col = ""
        for y in range(HEIGHT):
            current_col += text[y][x]
        if len(current_col.replace(".", "")) == 0:
            COLS.append(expand_by)
        else:
            COLS.append(1)
    ROWS = []
    for y in range(HEIGHT):
        if len(text[y].replace(".", "")) == 0:
            ROWS.append(expand_by)
        else:
            ROWS.append(1)

def shortest_distance(start: tuple, end: tuple) -> int:
    global ROWS, COLS
    y1 = min(start[1], end[1])
    y2 = max(start[1], end[1])
    height_difference = sum(ROWS[y1:y2])
    x1 = min(start[0], end[0])
    x2 = max(start[0], end[0])
    width_difference = sum(COLS[x1:x2])
    return height_difference + width_difference

galaxies = []
for y in range(HEIGHT):
    for x in range(WIDTH):
        if text[y][x] == "#":
            galaxies.append((x, y))

def sum_of_shortest_distances():
    distances = {}
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            if f"{i},{j}" in distances or f"{j},{i}" in distances:
                continue
            distances[f"{i},{j}"] = shortest_distance(galaxies[i], galaxies[j])
    return sum(distances.values())

expand_universe(2)
print(f"Part 1: {sum_of_shortest_distances()}")
expand_universe(1000000)
print(f"Part 2: {sum_of_shortest_distances()}")
