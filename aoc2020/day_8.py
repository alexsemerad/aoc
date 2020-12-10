#!/usr/bin/python3
import re
import copy

operation_regx = '^(\w+) (.*?)(\d+)$'


# -- Line -> List[(Tuple)] --
def parse_line(line):
    search_bag = re.search(operation_regx, line)
    operation  = search_bag.group(1)
    sign       = search_bag.group(2)
    argument   = search_bag.group(3)
    return (operation, sign, argument)


# -- Operators --
def operator(var_one, symbol, var_two):
    if symbol == '+':
        return int(var_one) + int(var_two)
    if symbol == '-':
        return int(var_one) - int(var_two)


# -- Clean Input --
file_input = 'input.txt'
with open(file_input, 'r', encoding='utf-8') as file:
    data = [parse_line(i) for i in file]


# -- PART 1 --
def handheld_halting(data):
    accumulator    = 0
    position       = 0
    seen_execution = []
    result         = ''
    while True:

        operation, sign, argument = data[position]
        if position in seen_execution:
            result = 'Infinite Loop reached.'
            break
        else:
            seen_execution.append(position)

        if operation == 'nop':
            position += 1

        elif operation == 'acc':
            accumulator = operator(accumulator, sign, argument)
            position += 1

        elif operation == 'jmp':
            position = operator(position, sign, argument)

        else:
            position += 1


        if position == len(data):
            result = 'End of program reached.'
            break

    return (result, accumulator)

print(handheld_halting(data))


# -- PART 2 --
values_changed = []
for i in range(len(data)):
    result = ''
    operation, sign, argument = data[i]
    if operation == 'nop':
        attempt = copy.copy(data)
        attempt[i] = ('jmp', sign, argument)
        result = handheld_halting(attempt)

        if result[0] == 'End of program reached.':
            print(i, result)

    elif operation == 'jmp':
        attempt = copy.copy(data)
        attempt[i] = ('nop', sign, argument)
        result = handheld_halting(attempt)

        if result[0] == 'End of program reached.':
            print(i, result)
