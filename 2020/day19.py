with open("day19.txt") as f:
    data = f.readlines()

ddata = [
    "0: 4 1",
    "1: 2 3 | 3 2",
    "2: 4 4 | 5 5",
    "3: 4 5 | 5 4",
    "4: \"a\"",
    "5: \"b\"",
    "6: 2 3",
    "7: 5 4",
    "",
    "ababbb",
    "bababa",
    "abbbab",
    "aaabbb",
    "aaaabbb"
]

# read rules
print("Reading rules...", end="")
rules = {}
i = 0
while data[i].strip() != "":
    line = data[i].strip()
    num, current_rule = line.split(":")
    num = int(num)
    current_rule = [r.strip() for r in current_rule.split("|")]
    if "\"" in current_rule[0]:
        current_rule = [current_rule[0][1]]
    rules[num] = current_rule
    i += 1

print("Done")

rules_options = {}
def eval_rule(rule_num):
    global rules_options
    if int(rule_num) in rules_options:
        return rules_options[int(rule_num)]
    print(f"Evaluating rule {rule_num}")
    rule = rules[int(rule_num)]
    result = []
    for option in rule:
        new_option = ""
        for part in option.split(" "):
            if part[0].isalpha():
                new_option += part
            elif part[0].isnumeric():
                new_option += str(eval_rule(int(part))).replace(" ", "")
            new_option += " "
        new_option = new_option.strip()
        lists = new_option.split(" ")
        if len(lists) > 1:
            lists = [f"{a}{b}" for a in eval(lists[0]) for b in eval(lists[1])]
        else:
            lists = lists[0]
        result.append(str(lists).replace(" ", ""))
    final = []
    for r in result:
        if r[0] == "[":
            l = eval(r)
            final.extend(l)
        else:
            final.append(r)
    rules_options[int(rule_num)] = final
    return final

print("Evaluating rules...")
for rule_num in rules:
    eval_rule(rule_num)
print("Evaluated rules.")

messages = data[i+1:]
#print(messages)
count = 0
for message in messages:
    if message.strip() in eval_rule(0):
        print(message.strip())
        count += 1
print(f"Part 1: {count}")
