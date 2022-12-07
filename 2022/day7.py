with open("day7.txt") as f:
    data = f.readlines()

ddata = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]

files = {}
dirs = []
path = "/"
for cmd in data:
    cmd = cmd.strip()
    cmd = cmd.split(" ")
    if cmd[0] == "$" and cmd[1] == "cd":
        if cmd[2] == "/":
            path = "/"
        elif cmd[2] == "..":
            p = path[1:-1].split("/")
            path = "/" + "/".join(p[:-1]) + "/"
        else:
            path += cmd[2] + "/"
        if path == "//":
            path = "/"
        if path not in dirs:
            dirs.append(path)
        #print(cmd, path)
    elif cmd[0] == "$" and cmd[1] == "ls":
        continue
    elif cmd[0] == "dir":
        continue
    else:
        files[path + cmd[1]] = int(cmd[0])

total_size = 0
dirs_size = {}
for d in dirs:
    size = 0
    for f in files:
        if f.startswith(d):
            size += files[f]
    dirs_size[d] = size
    if size <= 100000:
        total_size += size
print(f"Part 1: {total_size}")

size_dirs = {v: k for k, v in dirs_size.items()}
sizes = sorted(size_dirs.keys())
total_size = sizes[-1]
need = 40000000
for s in sizes:
    if total_size-s <= need:
        print(f"Part 2: {s}")
        break
