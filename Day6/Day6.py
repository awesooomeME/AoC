'''https://adventofcode.com/2022/day/6'''

def start_of_packet(num):
    with open("./Day6.txt") as f: lines = f.readline()
    for i in range(0,len(lines)-num-1):
        if len(set(lines[i:i+num]))==num:
            return i + num

print(start_of_packet(4))
print(start_of_packet(14))