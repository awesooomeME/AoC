'''https://adventofcode.com/2022/day/9'''

DIRECTIONS = {"R": 1+0j, "L": -1+0j, "U": -1j, "D": 1j}

def simulate_rope(length):
    rope = [0+0j]*length
    tail = set()
    with open("input/Day9.txt") as f: lines = f.readlines()
    for line in lines:
        direction, steps = line.strip().split()
        for _ in range(int(steps)):
            rope[0] += DIRECTIONS[direction]
            for i in range(1,length):
                distance = rope[i-1] - rope[i]
                #check if adjacent with each other
                if abs(distance) > abs(1+1j):
                    if not distance.imag == 0:
                        rope[i] += complex(0, distance.imag) / abs(distance.imag)
                    if not distance.real == 0:
                        rope[i] += distance.real / abs(distance.real)
            tail.add(rope[-1]) 
    return tail

print(len(simulate_rope(2)))
print(len(simulate_rope(10)))