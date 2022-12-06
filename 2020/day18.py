with open("day18.txt") as f:
    data = f.readlines()
test_data = [
    ["1 + 2 * 3 + 4 * 5 + 6", 71],
    ["1 + (2 * 3) + (4 * (5 + 6))", 51],
    ["2 * 3 + (4 * 5)", 26],
    ["5 + (8 * 3 + 9 + 3 * 4 * 3)", 437],
    ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240],
    ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632],
]

def parse(s):
    """
    given a string (s):
        if s contains only a single number:
            return eval(s)
        if s contains a single bracketed equation:
            return parse(s[1:-1]) (the equation without the outer brackets)
        find the first complete term (n1) and evaluate it
            a "complete term" is:
                a bracketed equation if the first character of `s` is a bracket
                a number otherwise
        the operator will be the character after the end of n1
        find the next complete term (n2) and evaluate it
        evaluate "n1 op n2"
        if the end of the string has been reached, return the answer
        otherwise, parse(answer + rest of string)
    """
    if debug:
        print("\tbegin", s)
    
    # if s has just one element, it must be a number
    if len(s.split(" ")) == 1:
        if debug:
            print(f"\tresult: [{s}]")
        return eval(s)
    
    # if s has outer brackets, re-parse without the brackets
    if s[0] == "(" and s[-1] == ")":
        brackets = 0
        for c in s[1:-1]:
            if c == "(":
                brackets += 1
            elif c == ")":
                brackets -= 1
            if brackets < 0:
                break
        if brackets == 0:
            return parse(s[1:-1])
    
    # calculate n1
    i = 0  # the current position in the string
    brackets = 0 # the number of unclosed brackets
    start = i # the starting position of n1
    end = None # the ending position of n1
    while i < len(s):
        if s[i] == "(":
            brackets += 1
        if s[i] == ")":
            brackets -= 1
        if s[i] == " " and brackets == 0:
            end = i
            break
        if s[i] == ")" and brackets == 0:
            end = i+1
            break
        i += 1
    n1 = parse(s[start:end])

    if end == len(s): # if we have finished parsing s, return
        return parse(s[1:-1])

    # find the operator
    op = s[end+1]

    # calculate n2
    brackets = 0
    start = end+3
    i = start
    while i < len(s):
        if i == len(s)-1:
            end = i+1
            break
        if s[i] == " " and brackets == 0:
            end = i
            break
        elif s[i] == "(":
            brackets += 1
        elif s[i] == ")":
            brackets -= 1
        i += 1
    n2 = parse(s[start:end])

    # calculate the result of (n1 op n2)
    if debug:
        print(f"\tresult: [{n1}] [{op}] [{n2}]", end="")
    result = eval(f"{n1}{op}{n2}")

    if end >= len(s)-1:
        if debug:
            print()
        return result
    else:
        if debug:
            print("\t... "+s[end+1:])
        return parse(str(result) + " " + s[end+1:])


def parse2(s):
    """
    given a string (s):
        if s contains only a single number:
            return eval(s)
        if s contains a single bracketed equation:
            return parse(s[1:-1]) (the equation without the outer brackets)
        find the first complete term (n1) and evaluate it
            a "complete term" is:
                a bracketed equation if the first character of `s` is a bracket
                a number otherwise
        the operator will be the character after the end of n1
        find the next complete term (n2) and evaluate it
        evaluate "n1 op n2"
        if the end of the string has been reached, return the answer
        otherwise, parse(answer + rest of string)
    """
    if debug:
        print("\tbegin", s)
    
    # if s has just one element, it must be a number
    if len(s.split(" ")) == 1:
        if debug:
            print(f"\tresult: [{s}]")
        return eval(s)
    
    # if s has outer brackets, re-parse without the brackets
    if s[0] == "(" and s[-1] == ")":
        brackets = 0
        for c in s[1:-1]:
            if c == "(":
                brackets += 1
            elif c == ")":
                brackets -= 1
            if brackets < 0:
                break
        if brackets == 0:
            return parse2(s[1:-1])
    
    # calculate n1
    i = 0  # the current position in the string
    brackets = 0 # the number of unclosed brackets
    start = i # the starting position of n1
    end = None # the ending position of n1
    while i < len(s):
        if s[i] == "(":
            brackets += 1
        if s[i] == ")":
            brackets -= 1
        if s[i] == " " and brackets == 0:
            end = i
            break
        if s[i] == ")" and brackets == 0:
            end = i+1
            break
        i += 1
    n1 = parse2(s[start:end])

    if end == len(s): # if we have finished parsing s, return
        return parse2(s[1:-1])

    # find the operator
    op = s[end+1]

    # calculate n2
    brackets = 0
    start = end+3
    i = start
    while i < len(s):
        if i == len(s)-1:
            end = i+1
            break
        if s[i] == " " and brackets == 0:
            end = i
            break
        elif s[i] == "(":
            brackets += 1
        elif s[i] == ")":
            brackets -= 1
        i += 1
    n2 = parse2(s[start:end])

    # calculate the result of (n1 op n2)
    if debug:
        print(f"\tresult: [{n1}] [{op}] [{n2}]", end="")
    result = eval(f"{n1}{op}{n2}")

    if end >= len(s)-1:
        if debug:
            print()
        return result
    else:
        if debug:
            print("\t... "+s[end+1:])
        return parse2(str(result) + " " + s[end+1:])

debug = False

if False:
    results = []
    for d in test_data:
        print(d[0])
        result = parse(d[0])
        results.append(result)
        print(f"{result} == {d[1]}\n")

if True:
    results = []
    for d in data:
        #print(d)
        result = parse(d.strip())
        results.append(result)
    print(f"Part 1: {sum(results)}")
