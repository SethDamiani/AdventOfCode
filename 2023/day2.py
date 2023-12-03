with open("day2.txt") as f:
    text = f.readlines()

color_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
total = 0
total2 = 0

for line in text:
    line = line.strip()
    game_number = int(line.split(":")[0].split(" ")[1])
    sets = line.split(":")[1].strip().split(";")
    maxes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    valid = True
    for s in sets:
        colors = s.split(",")
        for color in colors:
            num = int(color.strip().split(" ")[0])
            color_name = color.strip().split(" ")[1]
            if num > color_max[color_name]:
                valid = False
            maxes[color_name] = max(maxes[color_name], num)
    if valid:
        total += game_number
    power = maxes["red"] * maxes["green"] * maxes["blue"]
    total2 += power

print(total)
print(total2)
