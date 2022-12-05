with open("2020-17.txt") as f:
    data = f.readlines()
ddata = [
    ".#.",
    "..#",
    "###"
]

def generateSurrounding(x0, y0, z0):
    res = []
    for z in range(z0-1, z0+2):
        for y in range(y0-1, y0+2):
            for x in range(x0-1, x0+2):
                if not (x == x0 and y == y0 and z == z0):
                    res.append(f"{x} {y} {z}")
    return res

cycles = [{}]
size_xy = len(data[0].strip())
size_z = 1

for y in range(len(data)):
    for x in range(len(data[y].strip())):
        cycles[0][f"{x-1} {y-1} 0"] = data[y][x].strip()

for cycle in range(6):
    cycles.append({})
    for z in range(-1*size_z, size_z+1):
        for y in range(-1*size_xy, size_xy+1):
            for x in range(-1*size_xy, size_xy+1):
                current_location = f"{x} {y} {z}"
                #print("\nCurrent location: "+current_location)
                current = "."
                if current_location in cycles[-2] and cycles[-2][current_location] == "#":
                    current = "#"
                surrounding = generateSurrounding(x, y, z)
                count = 0
                for location in surrounding:
                    #print("\tChecking "+location, end="...")
                    if location in cycles[-2] and cycles[-2][location] == "#":
                        count += 1
                        #print("Found #", end="")
                    #print()
                if current == "#":
                    if 2 <= count <= 3:
                        new = "#"
                    else:
                        new = "."
                elif current == ".":
                    if count == 3:
                        new = "#"
                    else:
                        new = "."
                #print(f"Current={current} surrounding={count} new={new}")
                cycles[-1][current_location] = new
    size_xy += 1
    size_z += 1

for cycle in cycles:
    break
    print()
    print("-"*60)
    for z in range(-1*size_z, size_z+1):
        print(f"z={z}")
        for y in range(-1*size_xy, size_xy+1):
            for x in range(-1*size_xy, size_xy+1):
                current_location = f"{x} {y} {z}"
                if current_location in cycle and cycle[current_location] == "#":
                    print("#", end="")
                else:
                    print(".", end="")
            print()

count = 0
for s in cycles[-1]:
    if cycles[-1][s] == "#":
        count += 1
print(f"Part 1: {count}")

# ------ PART 2 -------

def generateSurrounding4(x0, y0, z0, w0):
    res = []
    for w in range(w0-1, w0+2):
        for z in range(z0-1, z0+2):
            for y in range(y0-1, y0+2):
                for x in range(x0-1, x0+2):
                    if not (x == x0 and y == y0 and z == z0 and w == w0):
                        res.append(f"{x} {y} {z} {w}")
    return res

cycles = [{}]
size_xy = len(data[0].strip())
size_zw = 1

for y in range(len(data)):
    for x in range(len(data[y].strip())):
        cycles[0][f"{x-1} {y-1} 0 0"] = data[y][x].strip()

for cycle in range(6):
    cycles.append({})
    for w in range(-1*size_zw, size_zw+1):
        for z in range(-1*size_zw, size_zw+1):
            for y in range(-1*size_xy, size_xy+1):
                for x in range(-1*size_xy, size_xy+1):
                    current_location = f"{x} {y} {z} {w}"
                    #print("\nCurrent location: "+current_location)
                    current = "."
                    if current_location in cycles[-2] and cycles[-2][current_location] == "#":
                        current = "#"
                    surrounding = generateSurrounding4(x, y, z, w)
                    count = 0
                    for location in surrounding:
                        #print("\tChecking "+location, end="...")
                        if location in cycles[-2] and cycles[-2][location] == "#":
                            count += 1
                            #print("Found #", end="")
                        #print()
                    if current == "#":
                        if 2 <= count <= 3:
                            new = "#"
                        else:
                            new = "."
                    elif current == ".":
                        if count == 3:
                            new = "#"
                        else:
                            new = "."
                    #print(f"Current={current} surrounding={count} new={new}")
                    cycles[-1][current_location] = new
    size_xy += 1
    size_zw += 1

for cycle in cycles:
    break
    print()
    print("-"*60)
    for z in range(-1*size_z, size_z+1):
        print(f"z={z}")
        for y in range(-1*size_xy, size_xy+1):
            for x in range(-1*size_xy, size_xy+1):
                current_location = f"{x} {y} {z}"
                if current_location in cycle and cycle[current_location] == "#":
                    print("#", end="")
                else:
                    print(".", end="")
            print()

count = 0
for s in cycles[-1]:
    if cycles[-1][s] == "#":
        count += 1
print(f"Part 2: {count}")

