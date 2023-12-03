def remove_non_symbols(s):
    return "".join([c for c in s if not c.isnumeric() and c != "."])

with open("day3.txt") as f:
    text = [l.strip() for l in f.readlines()]

text = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

total1 = 0
total2 = 0

numbers = []
for x in range(len(text)):
    line = []
    acc = ""
    for c in text[x]:
        if c.isnumeric():
            acc += c
        elif len(acc) > 0:
            line.append(acc)
            acc = ""
    numbers.append(line)

for n in range(len(text)):
    print(f"Row {n}")
    col = 0
    acc = ""
    start_index = 0
    end_index = 0
    while col < len(text[n]):
        current_char = text[n][col]
        if current_char.isnumeric():
            if len(acc) == 0:
                start_index = col
            acc += current_char
            col += 1
            if col < len(text[n]):
                continue
        if len(acc) > 0:
            end_index = col
        if acc != "":
            print(f"  {acc}:   {start_index} {end_index}")
            buffer_start = max(0, start_index-1)
            buffer_end = min(len(text[n])-1, end_index+1)
            is_part_number = False
            # check sides
            sides = remove_non_symbols(text[n][buffer_start:buffer_end])
            if len(sides) > 0:
                print(f"    beside {sides}")
                is_part_number = True
            if n > 0:
                above = remove_non_symbols(text[n-1][buffer_start:buffer_end])
                if len(above) > 0:
                    print(f"    above {above}")
                    is_part_number = True
            if n < len(text)-1:
                below = remove_non_symbols(text[n+1][buffer_start:buffer_end])
                if len(below) > 0:
                    print(f"    below {below}")
                    is_part_number = True
            if is_part_number:
                total1 += int(acc)
            else:
                print("  ----")

        acc = ""
        col += 1

print(f"\nPart 1: {total1}")
print(f"Part 2: {total2}")
