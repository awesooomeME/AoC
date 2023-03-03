'''https://adventofcode.com/2022/day/11'''

import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}

with open("./Day11.txt") as f: monkey_inputs = "".join(f.readlines()).split("\n\n")

# {items_inspected, items_to_inspect, operation, operation_value, test, test_if_true, test_if_false}
monkeys = []
for index, monkey in enumerate(monkey_inputs):
    monkeys.append({'inspected' : 0})
    first_line = ''.join(monkey.split('\n')[1].split(': ')[-1]).strip().split(', ')
    monkeys[index]['will_inspect'] = [int(item) for item in first_line]
    monkeys[index]['operation'] = ''.join(monkey.split('\n')[2].split('old ')[-1]).strip().split(' ')
    monkeys[index]['test'] = int(''.join(monkey.split('\n')[3]).strip().split('by ')[-1])
    monkeys[index]['test_if_true'] = int(''.join(monkey.split('\n')[4]).strip().split('throw to monkey ')[-1])
    monkeys[index]['test_if_false'] = int(''.join(monkey.split('\n')[5]).strip().split('throw to monkey ')[-1])

def simulate_monkey_business(rounds, worry_dampener):
    for i in range(rounds):
        for monkey in monkeys:
            for item in monkey['will_inspect']:
                monkey['inspected'] += 1 
                try:
                    new_worry_level = ops[monkey['operation'][0]](int(monkey['operation'][1]),item)
                except:
                    new_worry_level = ops[monkey['operation'][0]](item,item)
                monkey['will_inspect'] = monkey['will_inspect'][1:len(monkey['will_inspect'])]
                if (new_worry_level // worry_dampener) % monkey['test'] == 0:
                    monkeys[monkey['test_if_true']]['will_inspect'].append(new_worry_level // worry_dampener)
                else:
                    monkeys[monkey['test_if_false']]['will_inspect'].append(new_worry_level // worry_dampener)

    inspections =  [monkey['inspected'] for monkey in monkeys]

    monkey_business = max(inspections)
    inspections.remove(max(inspections))
    monkey_business *= max(inspections)
    return monkey_business

# print(simulate_monkey_business(20, 3))
print(simulate_monkey_business(1000, 1))