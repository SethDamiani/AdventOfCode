with open("2023/day5.txt") as f:
    text = [l.strip() for l in f.readlines()]

print("Get seeds")
seeds = text[0].split(":")[1].strip().split(" ")
seeds = [int(s) for s in seeds]

print("Get soil")
i = 3
seed_to_soil = {}
while len(text[i]) > 0:
    dest_start, source_start, length = [int(s) for s in text[i].split(" ")]
    for n in range(length):
        seed_to_soil[source_start] = dest_start
        source_start += 1
        dest_start += 1
    i += 1

print("Get fertilizer")
i += 2
soil_to_fertilizer = {}
while len(text[i]) > 0:
    dest_start, source_start, length = [int(s) for s in text[i].split(" ")]
    for n in range(length):
        soil_to_fertilizer[source_start] = dest_start
        source_start += 1
        dest_start += 1
    i += 1

print("Get water")
i += 2
fertilizer_to_water = {}
while len(text[i]) > 0:
    dest_start, source_start, length = [int(s) for s in text[i].split(" ")]
    for n in range(length):
        fertilizer_to_water[source_start] = dest_start
        source_start += 1
        dest_start += 1
    i += 1

print("Get light")
i += 2
water_to_light = {}
while len(text[i]) > 0:
    dest_start, source_start, length = [int(s) for s in text[i].split(" ")]
    for n in range(length):
        water_to_light[source_start] = dest_start
        source_start += 1
        dest_start += 1
    i += 1

print("Get temperature")
i += 2
light_to_temperature = {}
while len(text[i]) > 0:
    dest_start, source_start, length = [int(s) for s in text[i].split(" ")]
    for n in range(length):
        light_to_temperature[source_start] = dest_start
        source_start += 1
        dest_start += 1
    i += 1

print("Get humidity")
i += 2
temperature_to_humidity = {}
while len(text[i]) > 0:
    dest_start, source_start, length = [int(s) for s in text[i].split(" ")]
    for n in range(length):
        temperature_to_humidity[source_start] = dest_start
        source_start += 1
        dest_start += 1
    i += 1

print("Get location")
i += 2
humidity_to_location = {}
while i < len(text) and len(text[i]) > 0:
    dest_start, source_start, length = [int(s) for s in text[i].split(" ")]
    for n in range(length):
        humidity_to_location[source_start] = dest_start
        source_start += 1
        dest_start += 1
    i += 1

print("Begin Part 1")
part1 = 999999
for seed in seeds:
    soil = seed_to_soil[seed] if seed in seed_to_soil else seed
    fertilizer = soil_to_fertilizer[soil] if soil in soil_to_fertilizer else soil
    water = fertilizer_to_water[fertilizer] if fertilizer in fertilizer_to_water else fertilizer
    light = water_to_light[water] if water in water_to_light else water
    temperature = light_to_temperature[light] if light in light_to_temperature else light
    humidity = temperature_to_humidity[temperature] if temperature in temperature_to_humidity else temperature
    location = humidity_to_location[humidity] if humidity in humidity_to_location else humidity
    if location < part1:
        part1 = location
print(part1)
