'''https://adventofcode.com/2022/day/10'''

x = [1]
def part1():
    with open("./Day10.txt") as f: lines = f.readlines()
    for line in lines:
        instruction, *value = line.strip().split()
        if value:
            x.append(x[-1])
            x.append(x[-1] + int(value[0]))
        else:
            x.append(x[-1])

    print(x[19]*20 + x[59]*60 + x[99]*100  + x[139]*140 + x[179]*180 + x[219]*220)

def part2():
    counter = 1
    for val in x[1:]:
        if counter == val or counter == val - 1 or counter == val + 1:
            print("#",end="")
        else:
            print(".",end="")
        if counter == 40:
            print("\n",end="")
            counter -= 40
        counter += 1

part1()
part2()