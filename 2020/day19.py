with open("day19.txt") as f:
    data = f.readlines()

data = [
    "0: 4 1",
    "1: 2 3 | 3 2",
    "2: 4 4 | 5 5",
    "3: 4 5 | 5 4",
    "4: \"a\"",
    "5: \"b\"",
    "6: 2 3",
    "",
    "ababbb",
    "bababa",
    "abbbab",
    "aaabbb",
    "aaaabbb"
]

# read rules
rules = {}
i = 0
while data[i].strip() != "":
    line = data[i]
    rule_num, line = line.split(":")
    rule_num = int(rule_num)
    line = line.split(" ")[1:]
    rule = []
    r = []
    for c in line:
        if c == "|":
            rule.append(r)
            r = []
            continue
        try:
            r.append(int(c))
        except ValueError:
            r.append(c[1])
    rule.append(r)
    rules[rule_num] = rule
    i += 1

for rule in rules:
    break
    print(rule, rules[rule])

def eval_rule(rule_num):
    rule = rules[rule_num]
    if type(rule[0][0]) == str:
        return rule[0][0]
    
    # Expand rule
    result = []
    for r in rule:
        option = []
        for n in r:
            option.append(eval_rule(n))
        result.append(option)
    if type(result[0][0]) == str and len(result[0][0][0]) == 1:
        return ["".join(x) for x in result]
    finished = []
    for i in range(len(result)):
        cross = [f"{a}{b}" for a in result[i][0] for b in result[i][1]]
        finished.append(cross)
    if len(finished) == 1:
        return finished[0]
    return [f"{a}{b}" for a in finished[0] for b in finished[1]]

print(eval_rule(0))
exit(0)
messages = data[i+1:]
count = 0
for message in messages:
    if message.strip() in eval_rule(1):
        count += 1
print(f"Part 1: {count}")
