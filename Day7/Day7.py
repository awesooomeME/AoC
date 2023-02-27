'''https://adventofcode.com/2022/day/7'''

def get_dir(threshold, isPart1):
    dirs = {"/" : 0}
    cwd = ["/"]
    with open("./Day7.txt") as f: lines = f.readlines()
    for line in lines:
        line = line[:-1].split(" ")
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    cwd.pop(-1)
                elif line[2] == "/":
                    cwd = ["/"]
                else:
                    cwd.append(line[2])
        elif line[0] == "dir":
            dirs["".join(cwd) + line[1]] = 0
        else:
            dirs["".join(cwd)] += int(line[0])
            for i in range(1, len(cwd)):
                dirs["".join(cwd[:-i])] += int(line[0])

    if isPart1:    
        return sum(l for l in dirs.values() if l <= threshold)
    else:
        return min(l for l in dirs.values() if l >= dirs["/"] - 40000000)

print(get_dir(100000, True))
print(get_dir(0, False))
            

