total_1 = 0
total_2 = 0
scores = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}
with open("day2.txt") as f:
    ff = [
        "A Y",
        "B X",
        "C Z"
    ]
    for line in f:
        line = line.split(" ")
        op = line[0].strip()
        me = line[1].strip()
        # part 1
        total_1 += scores[me]
        if (op == "A" and me == "X") or (op == "B" and me == "Y") or (op == "C" and me == "Z"):
            total_1 += 3
        elif (op == "A" and me == "Y") or (op == "B" and me == "Z") or (op == "C" and me == "X"):
            total_1 += 6
        # part 2
        if me == "X":
            #lose
            moves = {
                "A": "Z",
                "B": "X",
                "C": "Y"
            }
        elif me == "Y":
            # tie
            total_2 += 3
            moves = {
                "A": "X",
                "B": "Y",
                "C": "Z"
            }
        else:
            #win
            total_2 += 6
            moves = {
                "A": "Y",
                "B": "Z",
                "C": "X"
            }
        total_2 += scores[moves[op]]
    print(f"Part 1: {total_1}\nPart 2: {total_2}")
