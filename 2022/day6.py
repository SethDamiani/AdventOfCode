with open("day6.txt") as f:
    data = f.readlines()[0].strip()

ddata = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
loc = 0
for i in range(3, len(data)):
    last_four = list(data[i-3:i+1])
    last_four_unique = list(set(list(last_four)))
    #print(last_four, last_four_unique)
    if len(last_four_unique) == len(last_four):
        loc = i+1
        break

print(loc)

loc = 0
for i in range(13, len(data)):
    last_four = list(data[i-13:i+1])
    last_four_unique = list(set(list(last_four)))
    #print(last_four, last_four_unique)
    if len(last_four_unique) == len(last_four):
        loc = i+1
        break

print(loc)
