puzzle = "1,0,15,2,10,13"
#puzzle = "0,3,6"
p = [int(x) for x in puzzle.split(",")]
mem = {p[i]: [i+1] for i in range(len(p))}

last_num = p[-1]
turn = len(p)+1

while turn <= 30000000:
    if len(mem[last_num]) < 2:
        last_num = 0
    else:
        last_num = mem[last_num][-1] - mem[last_num][-2]
    if last_num not in mem:
        mem[last_num] = []
    mem[last_num].append(turn)
    #print(f"{turn}: {last_num}")
    turn += 1
#print(mem)
print(last_num)