from typing import Optional


text = [[p for p in l.strip()] for l in open("2023/day10.txt").readlines()]
width = len(text[0])
height = len(text)

points_in_loop = []

def find_next(current_location: tuple, previous_location: Optional[tuple] = None) -> tuple:
    y, x = current_location

    if not previous_location:
        # is starting position
        if x < width - 1 and text[y][x+1] in ["J", "-", "7"]:
            return x+1, y
        elif x > 0 and text[y][x-1] in ["F", "-", "L"]:
            return x-1, y
        elif y < height-1 and text[y+1][x] in ["L", "|", "J"]:
            return x, y+1
        elif y > 0 and text[y-1][x] in ["F", "|", "7"]:
            return x, y-1
        raise Exception(f"Can't find next for starting position. {current_location=}")

    GO_UP = x, y-1
    GO_DOWN = x, y+1
    GO_LEFT = x-1, y
    GO_RIGHT = x+1, y
    py, px = previous_location
    if y < py:
        came_from = "below"
    elif y > py:
        came_from = "above"
    elif x < px:
        came_from = "right"
    elif x > px:
        came_from = "left"
    else:
        raise Exception("Current and prev locations are the same.")
    
    current_pipe = text[y][x]
    if current_pipe == "J":
        if came_from == "left":
            return GO_UP
        elif came_from == "above":
            return GO_LEFT
    if current_pipe == "|":
        if came_from == "below":
            return GO_UP
        if came_from == "above":
            return GO_DOWN
    if current_pipe == "-":
        if came_from == "left":
            return GO_RIGHT
        if came_from == "right":
            return GO_LEFT
    if current_pipe == "L":
        if came_from == "above":
            return GO_RIGHT
        if came_from == "right":
            return GO_UP
    if current_pipe == "7":
        if came_from == "below":
            return GO_LEFT
        if came_from == "left":
            return GO_DOWN
    if current_pipe == "F":
        if came_from == "bottom":
            return GO_RIGHT
        if came_from == "right":
            return GO_DOWN
    raise Exception(f"Can't find next. {previous_location=} {current_location=} {current_pipe=}")


# find start location
start_location = None
for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j] == "S":
            start_location = (j, i)
print(f"Start: {start_location}")


