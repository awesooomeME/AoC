'''https://adventofcode.com/2022/day/5'''

stacks = [["B","S","V","Z","G","P","W"],
          ["J","V","B","C","Z","F"],
          ["V","L","M","H","N","Z","D","C"],
          ["L","D","M","Z","P","F","J","B"],
          ["V","F","C","G","J","B","Q","H"],
          ["G","F","Q","T","S","L","B"],
          ["L","G","C","Z","V"],
          ["N","L","G"],
          ["J","F","H","C"]]

def part1():
    with open("input/Day5.txt") as f: lines = f.readlines()
    for line in lines:
        for i in range(0,int(line.split(" ")[1])):
            temp = stacks[int(line.split(" ")[3])-1].pop(-1)
            stacks[int(line.split(" ")[5])-1].append(temp)

    topStack = ""
    for stack in stacks:
        topStack += stack.pop(-1)
    return topStack

def part2():
    with open("input/Day5.txt") as f: lines = f.readlines()
    for line in lines:
        temp = []
        for i in range(0,int(line.split(" ")[1])):
            temp.append(stacks[int(line.split(" ")[3])-1].pop(-1))

        for i in reversed(temp):    
            stacks[int(line.split(" ")[5])-1].append(i)

    topStack = ""
    for stack in stacks:
        topStack += stack.pop(-1)
    return topStack

print(part1())

stacks = [["B","S","V","Z","G","P","W"],
          ["J","V","B","C","Z","F"],
          ["V","L","M","H","N","Z","D","C"],
          ["L","D","M","Z","P","F","J","B"],
          ["V","F","C","G","J","B","Q","H"],
          ["G","F","Q","T","S","L","B"],
          ["L","G","C","Z","V"],
          ["N","L","G"],
          ["J","F","H","C"]]

print(part2())      