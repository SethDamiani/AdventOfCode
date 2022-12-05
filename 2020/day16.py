with open("2020-16.txt") as f:
    data = f.readlines()
ddata = [
    "class: 1-3 or 5-7\n",
    "row: 6-11 or 33-44\n",
    "seat: 13-40 or 45-50\n",
    "\n",
    "your ticket:\n",
    "7,1,14\n",
    "\n",
    "nearby tickets:\n",
    "7,3,47\n",
    "40,4,50\n",
    "55,2,20\n",
    "38,6,12\n"
]

ddata = [
    "class: 0-1 or 4-19\n",
    "row: 0-5 or 8-19\n",
    "seat: 0-13 or 16-19\n",
    "\n",
    "your ticket:\n",
    "11,12,13\n",
    "\n",
    "nearby tickets:\n",
    "3,9,18\n",
    "15,1,5\n",
    "5,14,9\n"
]

fields = {}
yours = []
nearby = []
nearby_valid = []

line_i = 0
line = data[0]

# read fields
while line != "\n":
    line = line.split(":")
    name = line[0].strip()
    line = line[1].strip().split(" or ")
    range_1 = [int(x) for x in line[0].strip().split("-")]
    range_2 = [int(x) for x in line[1].strip().split("-")]
    fields[name] = {
        "name": name,
        "ranges": [range_1, range_2],
        "field_nums": []
    }
    line_i += 1
    line = data[line_i]

# read yours
line_i += 2
yours = [int(x) for x in data[line_i].strip().split(",")]
line_i += 3

# read nearby
while line_i < len(data):
    nearby.append([int(x) for x in data[line_i].strip().split(",")])
    line_i += 1

# part 1
total = 0
for ticket in nearby:
    ticket_valid = True
    for i in ticket:
        valid = False
        for field in fields:
            r1 = fields[field]["ranges"][0]
            r2 = fields[field]["ranges"][1]
            if r1[0] <= i <= r1[1] or r2[0] <= i <= r2[1]:
                valid = True
                break
        if not valid:
            total += i
            ticket_valid = False
    if ticket_valid:
        nearby_valid.append(ticket)
print(f"Part 1: {total}")

# generate possible field nums
for field in fields:
    r1 = fields[field]["ranges"][0]
    r2 = fields[field]["ranges"][1]
    for i in range(len(yours)):
        i_valid = True
        for ticket in nearby_valid:
            if not (r1[0] <= ticket[i] <= r1[1] or r2[0] <= ticket[i] <= r2[1]):
                i_valid = False
                break
        if i_valid:
            fields[field]["field_nums"].append(i)

# reduce possibilities until one left for each field
only_singles = False
while not only_singles:
    only_singles = True
    for field in fields:
        if len(fields[field]["field_nums"]) == 1:
            remaining = fields[field]["field_nums"][0]
            for field1 in fields:
                if field1 != field and remaining in fields[field1]["field_nums"]:
                    fields[field1]["field_nums"].remove(remaining)
        else:
            only_singles = False

# multiply values together:
product = 1
for field in fields:
    if "departure" in field:
        product *= yours[fields[field]["field_nums"][0]]

print(f"Part 2: {product}")
