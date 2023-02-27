'''https://adventofcode.com/2022/day/4'''

def checkOverlap(isFullOverlap):
    with open("./Day4.txt") as f: lines = f.readlines()
    num = 0
    for line in lines:
        pair1, pair2 = line.split(",")
        first_range = set(range(int(pair1.split("-")[0]),int(pair1.split("-")[1])+1))
        second_range = set(range(int(pair2.split("-")[0]),int(pair2.split("-")[1])+1))
        if isFullOverlap:
            if  first_range >= second_range or second_range >= first_range:
                num += 1
        else:
            if  first_range & second_range:
                num += 1
    return num

print(checkOverlap(True))
print(checkOverlap(False))