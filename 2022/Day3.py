'''https://adventofcode.com/2022/day/3'''

def part1():
    with open("input/Day3.txt") as f: lines=f.readlines()
    score = 0
    for line in lines:
        ls = []
        ls.append(line[:len(line)//2].strip())
        ls.append(line[len(line)//2:].strip())
        if (list(set(ls[0]) & set(ls[1]))[0]).islower():
            score += ord(list(set(ls[0]) & set(ls[1]))[0]) - 96
        else:
            score += ord(list(set(ls[0]) & set(ls[1]))[0]) - 38
    return score  

def part2():
    with open("input/Day3.txt") as f: lines=f.readlines()
    score = 0
    for i in range(0,len(lines),3):
        ls = []
        ls.append(lines[i].strip())
        ls.append(lines[i+1].strip())
        ls.append(lines[i+2].strip())
        if (list(set(ls[0]) & set(ls[1]) & set(ls[2]))[0]).islower():
            score += ord(list(set(ls[0]) & set(ls[1]) & set(ls[2]))[0]) - 96
        else:
            score += ord(list(set(ls[0]) & set(ls[1]) & set(ls[2]))[0]) - 38
    return score  
    

print(part1())
print(part2())