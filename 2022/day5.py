import copy

with open("day5.txt") as f:
    data = f.readlines()
ddata = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2"
]

i = 0
stacks = {}
while data[i].strip() != "":
    line = data[i].strip()
    for n in range(len(line)):
        if line[n].isalpha():
            stack = ((n-1)//4)+1
            if stack not in stacks:
                stacks[stack] = []
            stacks[stack].insert(0, line[n])
    i += 1

stacks2 = copy.deepcopy(stacks)

for stack in stacks:
    print(stack, stacks[stack])

i += 1

while i < len(data):
    line = data[i].split(" ")
    number_of_boxes = int(line[1])
    from_stack = int(line[3])
    to_stack = int(line[5])
    temp = []
    for n in range(number_of_boxes):
        box = stacks[from_stack][-1]
        box2 = stacks2[from_stack][-1]
        del stacks[from_stack][-1]
        del stacks2[from_stack][-1]
        stacks[to_stack].append(box)
        temp.append(box2)
    stacks2[to_stack].extend(temp[::-1])
    i += 1

print()
for stack in stacks:
    print(stack, stacks[stack])

sorted_stacks = sorted(stacks.keys())
message = ""
message2 = ""
for stack in sorted_stacks:
    message += stacks[stack][-1]
    message2 += stacks2[stack][-1]
print(f"Part 1: {message}")
print(f"Part 2: {message2}")
