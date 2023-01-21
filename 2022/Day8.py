'''https://adventofcode.com/2022/day/8'''

with open("input/Day8.txt") as f:  lines = f.readlines()
grid = [line.split("\n")[0] for line in lines]

def part1(row, col):
    if row==0 or col==0 or row==len(grid)-1 or col==len(grid[0])-1:
        return True
    else:
        #left
        if max([grid[row][i] for i in range(0,col)]) < grid[row][col]:
            return True
        if max([grid[row][i] for i in range(col+1,len(grid[0]))]) < grid[row][col]:
            return True
        if max([grid[i][col] for i in range(0,row)]) < grid[row][col]:
            return True
        if max([grid[i][col] for i in range(row+1,len(grid))]) < grid[row][col]:
            return True
        return False

def part2(row,col):
    if row==0 or col==0 or row==len(grid)-1 or col==len(grid[0])-1:
        return 0
    else:
        score = 1
        multiplier = 0
        for i in reversed(range(0,col)):
            if grid[row][i] < grid[row][col]:
                multiplier += 1
            else:
                multiplier += 1
                break
        score *= multiplier
        multiplier = 0

        for i in range(col+1,len(grid)):
            if grid[row][i] < grid[row][col]:
                multiplier += 1
            else:
                multiplier += 1
                break
        score *= multiplier
        multiplier = 0
        
        for i in reversed(range(0,row)):
            if grid[i][col] < grid[row][col]:
                multiplier += 1
            else:
                multiplier += 1
                break
        score *= multiplier
        multiplier = 0

        for i in range(row+1,len(grid[0])):
            if grid[i][col] < grid[row][col]:
                multiplier += 1
            else:
                multiplier += 1
                break
        score *= multiplier
        
        return score
        


sum = 0
scores = []
for i in range(0,len(grid)):
    for j in range(0,len(grid[0])):
        if part1(i, j):
            sum += 1
        scores.append(part2(i, j))
print(sum)
print(max(scores))