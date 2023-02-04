with open("day8.txt") as f:
    data = f.readlines()
data = [x.strip() for x in data]
data = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390"
]

def check(y, x, debug=False):
    #if x == 0 or y == 0 or x == len(data[y]) or y == len(data):
    #    return True
    tree = int(data[y][x])
    #left
    left = True
    for i in range(x-1, -1, -1):
        curr = int(data[y][i])
        if debug:
            print("checking", y, i, curr, end="")
        if tree <= curr:
            if debug:
                print(" not left", end="")
            left = False
        if debug:
            print()
    right = True
    for i in range(x+1, len(data[y])):
        curr = int(data[y][i])
        if debug:
            print("checking", y, i, curr, end="")
        if tree <= curr:
            if debug:
                print(" not right", end="")
            right = False
        if debug:
            print()
    top = True
    for j in range(y-1, -1, -1):
        if debug:
            print("checking", y, i, end="")
        curr = int(data[j][x])
        if tree <= curr:
            if debug:
                print(" not top", end="")
            top = False
        if debug:
            print()
    bottom = True
    for j in range(y+1, len(data)):
        if debug:
            print("checking", y, i, end="")
        curr = int(data[j][x])
        if tree <= curr:
            if debug:
                print(" not bottom", end="")
            bottom = False
        if debug:
            print()
    return left or right or top or bottom

def check2(y, x, debug=False):
    #if x == 0 or y == 0 or x == len(data[y]) or y == len(data):
    #    return True
    tree = int(data[y][x])
    result = 1
    left = 0
    high = 0
    for i in range(x-1, -1, -1):
        curr = int(data[y][i])
        if curr > high:
            left += 1
            high = curr
        if debug:
            print("checking", y, i, curr, end="")
        if curr >= tree:
            if debug:
                print(" not left", end="")
            break
        if debug:
            print()
    right = 0
    high = 0
    for i in range(x+1, len(data[y])):
        curr = int(data[y][i])
        if curr > high:
            right += 1
            print("add right", y, i)
            high = curr
        if tree <= curr:
            break
    top = 0
    high = 0
    for j in range(y-1, -1, -1):
        if debug:
            print("checking", y, i, end="")
        curr = int(data[j][x])
        if curr > high:
            top += 1
            high = curr
        if tree <= curr:
            if debug:
                print(" not top", end="")
            break
        if debug:
            print()
    bottom = 0
    high = 0
    for j in range(y+1, len(data)):
        if debug:
            print("checking", y, i, end="")
        curr = int(data[j][x])
        if curr > high:
            bottom += 1
            high = curr
        if tree <= curr:
            if debug:
                print(" not bottom", end="")
            break
        if debug:
            print()
    print("\n", left, right, top, bottom)
    return left * right * top * bottom

count = 0
best = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if check(i, j):
            #print(f"{i},{j} visible")
            count += 1
        score = check2(i, j)
        if score > best:
            best = score
#print(f"bottom: {count}")

#print(count, best)
print(check2(3,2,True))
