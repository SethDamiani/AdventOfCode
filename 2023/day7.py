with open("2023/day7.txt") as f:
    text = [l.strip() for l in f.readlines()]

m = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def key(string):
    if " " in string:
        string = string.split(" ")[0]
    total = 0
    cards = sorted([string.count(symbol) for symbol in list(set(string))])
    if cards == [5]:
        total += 70000000000000
    elif cards == [1, 4]:
        total += 60000000000000
    elif cards == [2, 3]:
        total += 50000000000000
    elif cards == [1, 1, 3]:
        total += 40000000000000
    elif cards == [1, 2, 2]:
        total += 30000000000000
    elif cards == [1, 1, 1, 2]:
        total += 20000000000000
    elif cards == [1, 1, 1, 1, 1]:
        total += 10000000000000
    for i in range(len(string)):
        total += (100 ** (len(string) - i)) * (m.index(string[i])+1)
    return total

p1_list = sorted(text, key=key)
print(p1_list)
part1 = 0
for i in range(len(p1_list)):
    part1 += int(p1_list[i].split(" ")[1]) * (i+1)
print(part1)
