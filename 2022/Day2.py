'''https://adventofcode.com/2022/day/2'''

def choicePoints(choice):
    if choice == "X":
        return 1
    elif choice == "Y":
        return 2
    elif choice == "Z":
        return 3

def part1():
    with open("input/Day2.txt") as f: lines = f.readlines()
    score = 0
    for line in lines:
        diff = ord(line[2]) - ord(line[0]) 
        if diff == 23:
            score += 3
        elif diff == 24 or diff == 21:
            score += 6
        elif diff == 25 or diff == 22:
            pass
        score += choicePoints(line[2])
    return score

def part2():
    with open("input/Day2.txt") as f: lines = f.readlines()
    score = 0
    for line in lines:
        if line[2] == "X":
            score += 0
            if line[0] == "A":
                score += choicePoints(chr(ord(line[0]) + 25))
            else:
                score += choicePoints(chr(ord(line[0]) + 22))
        elif line[2] == "Y":
            score += 3
            score += choicePoints(chr(ord(line[0]) + 23))
        elif line[2] == "Z":
            score += 6
            if line[0] == "C":
                score += choicePoints(chr(ord(line[0]) + 21))
            else:
                score += choicePoints(chr(ord(line[0]) + 24))
    return score

print(part1())
print(part2())