with open("day10.txt") as f:
    data = f.readlines()

def do_cycle():
    global cycle
    global total
    global col
    if cycle == 20 or (cycle-20)%40 == 0:
        total += x * cycle
    pixel = "#" if x-1 <= col <= x+1 else " "
    print(pixel, end="")
    col += 1
    if col > 39:
        print()
        col = 0
    cycle += 1

total = 0
cycle = 1
x = 1
col = 0
for line in data:
    do_cycle()
    line = line.strip()
    if line.startswith("addx"):
        do_cycle()
        x += int(line.split(" ")[1])


print(total)
