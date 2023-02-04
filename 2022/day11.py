with open("day11.txt") as f:
    data = f.readlines()

monkeys = []
i = 0
while i <= len(data):
    i += 1
    items = data[i].strip().split(":")[1].strip().split(", ")
    items = [int(x) for x in items]
    i += 1
    operation = data[i].strip().split("=")[1].strip()
    i += 1
    divisible = int(data[i].strip().split(" ")[-1])
    i += 1
    true = int(data[i].strip().split(" ")[-1])
    i += 1
    false = int(data[i].strip().split(" ")[-1])
    i += 2
    monkeys.append({
        "items": items,
        "operation": operation,
        "divisible": divisible,
        "true": true,
        "false": false,
        "inspections": 0
    })

for round in range(20):
    for m in range(len(monkeys)):
        for old in monkeys[m]["items"]:
            monkeys[m]["inspections"] += 1
            answer = eval(monkeys[m]["operation"]) // 3
            if answer % monkeys[m]["divisible"] == 0:
                destination = monkeys[m]["true"]
            else:
                destination = monkeys[m]["false"]
            monkeys[destination]["items"].append(answer)
        monkeys[m]["items"] = []

inspections = sorted([m["inspections"] for m in monkeys])
part1 = inspections[-1] * inspections[-2]
print(f"Part 1: {part1}")

for round in range(10000):
    for m in range(len(monkeys)):
        for old in monkeys[m]["items"]:
            monkeys[m]["inspections"] += 1
            answer = eval(monkeys[m]["operation"])
            if answer % monkeys[m]["divisible"] == 0:
                destination = monkeys[m]["true"]
            else:
                destination = monkeys[m]["false"]
            monkeys[destination]["items"].append(answer)
        monkeys[m]["items"] = []

inspections = sorted([m["inspections"] for m in monkeys])
part2 = inspections[-1] * inspections[-2]
print(f"Part 2: {part2}")
