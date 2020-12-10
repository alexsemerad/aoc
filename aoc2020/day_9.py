#!/usr/bin/python3
import itertools


# -- Open File --
file_input = 'input.txt'

with open(file_input, 'r', encoding='utf-8') as file:
    input = [int(i.strip()) for i in file]


# -- Part 1 --
XMAS_1 = []
for i in range(25, len(input)):
    combinatorials = itertools.combinations(set(input[i-25:i]), 2)
    validation = [sum(x) == input[i] for x in combinatorials]
    if not any(validation):
        XMAS_1.append((i, input[i]))

print(XMAS_1[0])


# -- Part 2 --
position  = XMAS_1[0][0] #<-- position of solution 1
target    = XMAS_1[0][1] #<-- N° solution 1

def contiguous_set(input):
    for i in range(len(input)):
        total = 0
        for x in range(25):
            try:
                total += input[i+x]
                if total == target:
                    return (i, x)
                if total > target:
                    break
            except IndexError:
                pass

position, range_num = contiguous_set(input)
XMAS_2 = [input[position+i] for i in range(range_num)]

print(min(XMAS_2) + max(XMAS_2))
