'''https://adventofcode.com/2022/day/1'''

def countCalories(num=1):
    with open("./Day1.txt") as f: lines = f.readlines()
    calories = []
    calory = 0
    for line in lines:
        if line.strip() == "":
            calories.append(calory)
            calory = 0
        else:
            calory += int(line.strip())
    sum = 0
    
    for i in range(0,num-1):
        index = calories.index(max(calories))
        sum += calories.pop(index)
    
    return sum

print(countCalories(2))
print(countCalories(4))