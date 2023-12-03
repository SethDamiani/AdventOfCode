from functools import cmp_to_key

def compare(one, two) -> int:
    if type(one) == str:
        one = eval(one)
        two = eval(two)
    #print(f"comparing {one} and {two}")
    if type(one) == int and type(two) == int:
        if one < two:
            return -1
        if one > two:
            return 1
        return 0
    if type(one) == list and type(two) == list:
        for i in range(len(one)):
            try:
                result = compare(one[i], two[i])
            except IndexError:
                return 1
            if result != 0:
                return result
        if len(one) < len(two):
            return -1
        return 0
    if type(one) == int and type(two) == list:
        return compare([one], two)
    if type(one) == list and type(two) == int:
        return compare(one, [two])
    raise Exception

with open("2022/day13.txt") as f:
    text = [l.strip() for l in f.readlines()]

text1 = [
    "[1,1,3,1,1]",
    "[1,1,5,1,1]",
    "",
    "[[1],[2,3,4]]",
    "[[1],4]",
    "",
    "[9]",
    "[[8,7,6]]",
    "",
    "[[4,4],4,4]",
    "[[4,4],4,4,4]",
    "",
    "[7,7,7,7]",
    "[7,7,7]",
    "",
    "[]",
    "[3]",
    "",
    "[[[]]]",
    "[[]]",
    "",
    "[1,[2,[3,[4,[5,6,7]]]],8,9]",
    "[1,[2,[3,[4,[5,6,0]]]],8,9]",
]

index = 0
part1 = 0
while index*3+1 < len(text):
    i = index * 3
    one = eval(text[i])
    two = eval(text[i+1])
    result = compare(one, two)
    if result == -1:
        part1 += index+1
    index += 1
print(part1)

p2_list = [x for x in text if len(x) != 0]
p2_list.append("[[2]]")
p2_list.append("[[6]]")
p2_sorted = sorted(p2_list, key=cmp_to_key(compare))
location_of_divider_1 = p2_sorted.index("[[2]]")+1
location_of_divider_2 = p2_sorted.index("[[6]]")+1
print(location_of_divider_1 * location_of_divider_2)
