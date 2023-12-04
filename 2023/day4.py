with open("2023/day4.txt") as f:
    text = [l.strip() for l in f.readlines()]

text1 = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

part1 = 0
part2 = 0
p2_tracker = {}
for i in range(len(text)):
    p2_tracker[i+1] = 1
for line in text:
    card_number, line = line.split(":")
    card_number = [c for c in card_number.split(" ") if len(c) > 0]
    card_number = int(card_number[1])
    line = line.strip()
    winning_numbers, my_numbers = line.split("|")
    winning_numbers = [int(n) for n in winning_numbers.strip().split(" ") if len(n) > 0]
    my_numbers = [int(n) for n in my_numbers.strip().split(" ") if len(n) > 0]
    shared_numbers = [n for n in winning_numbers if n in my_numbers]
    if len(shared_numbers) > 0:
        points = 1
        for i in range(len(shared_numbers) - 1):
            points *= 2
        #print(line, "     ", shared_numbers, "    ", points)
        part1 += points
    for i in range(len(shared_numbers)):
        p2_tracker[card_number+i+1] += p2_tracker[card_number]

for i in p2_tracker:
    part2 += p2_tracker[i]

print(part1)
print(part2)
