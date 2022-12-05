with open("2020-14.txt") as f:
    ff = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0"
    ]
    mask = ""
    mem = {}
    for line in f:
        line = line.split(" ")
        if line[0] == "mask":
            mask = line[2].strip()
        else:
            addr = int(line[0].split("[")[1][:-1])
            val = int(line[2])
            bin_val = "{0:b}".format(val)
            masked_val = ""
            for i in range(len(mask)):
                i_x = i*-1 - 1
                masked_bit = mask[i_x]
                if i < len(bin_val) and masked_bit == "X":
                    real_bit = bin_val[i_x]
                elif masked_bit != "X":
                    real_bit = masked_bit
                else:
                    real_bit = "0"
                masked_val = real_bit + masked_val
            mem[addr] = int(masked_val, 2)
    print(f"Part 1: {sum(mem.values())}")

with open("2020-14.txt") as f:
    ff = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1"
    ]
    mem = {}
    mask = ""
    for line in f:
        #print(line)
        line = line.split(" ")
        if line[0] == "mask":
            mask = line[2].strip()
        else:
            addr_int = int(line[0].split("[")[1][:-1])
            addr_bin = "{0:b}".format(addr_int)
            val = int(line[2])
            addr_masked = ""
            for i in range(len(mask)):
                i_x = i*-1 - 1
                if mask[i_x] == "1":
                    real_bit = "1"
                elif mask[i_x] == "0":
                    real_bit = addr_bin[i_x] if i < len(addr_bin) else "0"
                elif mask[i_x] == "X":
                    real_bit = "X"
                addr_masked = real_bit + addr_masked
            float_count = addr_masked.count("X")
            xs = "0"*float_count
            while len(xs) <= float_count:
                #print("\t"+xs)
                temp_addr = ""
                x_count = 0
                for i in range(len(addr_masked)):
                    if addr_masked[i] == "X":
                        temp_addr += xs[x_count]
                        x_count += 1
                    else:
                        temp_addr += addr_masked[i]
                mem[temp_addr] = val
                xs = bin(int(xs, 2) + 1)[2:]
                while len(xs) < float_count:
                    xs = "0"+xs
                #print("\t\t"+xs)
    print(f"Part 2: {sum(mem.values())}")
