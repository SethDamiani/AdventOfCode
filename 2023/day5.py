with open("2023/day5.txt") as f:
    text = [l.strip() for l in f.readlines()]

print("Get seeds")
seeds = text[0].split(":")[1].strip().split(" ")
seeds = [int(s) for s in seeds]

print("Get soil")
i = 3
seed_to_soil = []
while len(text[i]) > 0:
    seed_to_soil.append([int(s) for s in text[i].split(" ")])
    i += 1

print("Get fertilizer")
i += 2
soil_to_fertilizer = []
while len(text[i]) > 0:
    soil_to_fertilizer.append([int(s) for s in text[i].split(" ")])
    i += 1

print("Get water")
i += 2
fertilizer_to_water = []
while len(text[i]) > 0:
    fertilizer_to_water.append([int(s) for s in text[i].split(" ")])
    i += 1

print("Get light")
i += 2
water_to_light = []
while len(text[i]) > 0:
    water_to_light.append([int(s) for s in text[i].split(" ")])
    i += 1

print("Get temperature")
i += 2
light_to_temperature = []
while len(text[i]) > 0:
    light_to_temperature.append([int(s) for s in text[i].split(" ")])
    i += 1

print("Get humidity")
i += 2
temperature_to_humidity = []
while len(text[i]) > 0:
    temperature_to_humidity.append([int(s) for s in text[i].split(" ")])
    i += 1

print("Get location")
i += 2
humidity_to_location = []
while i < len(text) and len(text[i]) > 0:
    humidity_to_location.append([int(s) for s in text[i].split(" ")])
    i += 1

master_map = {
    "seed_to_soil": {},
    "soil_to_fertilizer": {},
    "fertilizer_to_water": {},
    "water_to_light": {},
    "light_to_temperature": {},
    "temperature_to_humidity": {},
    "humidity_to_location": {},
}
def translate(map, value, name):
    if value in master_map[name]:
        return master_map[name][value]
    for m in map:
        if m[1] <= value <= m[1]+m[2]:
            result = m[0] + value - m[1]
            master_map[name][value] = result
            return result
    master_map[name][value] = value
    return value

done_map = {}
def seed_to_location(seed):
    if seed in done_map:
        return done_map[seed]
    soil = translate(seed_to_soil, seed, "seed_to_soil")
    fertilizer = translate(soil_to_fertilizer, soil, "soil_to_fertilizer")
    water = translate(fertilizer_to_water, fertilizer, "fertilizer_to_water")
    light = translate(water_to_light, water, "water_to_light")
    temperature = translate(light_to_temperature, light, "light_to_temperature")
    humidity = translate(temperature_to_humidity, temperature, "temperature_to_humidity")
    location = translate(humidity_to_location, humidity, "humidity_to_location")
    done_map[seed] = location
    return location

print("Begin Part 1")
part1 = 999999999999999999999999999999
for seed in seeds:
    location = seed_to_location(seed)
    #print(seed, soil, fertilizer, water, light, temperature, humidity, location)
    if location < part1:
        part1 = location
print(part1)

part2 = 999999999999999999999999999999
for n in range(0, len(seeds), 2):
    print(f"Part 2: {seeds[n]} to {seeds[n]+seeds[n+1]}")
    for i in range(seeds[n+1]):
        seed = seeds[n] + i
        location = seed_to_location(seed)
        if location < part2:
            part2 = location
print(part2)
