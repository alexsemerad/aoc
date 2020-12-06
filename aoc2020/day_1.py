#!/usr/bin/python3

import itertools

# -- Open File --
file_input = 'input.txt'

with open(file_input, 'r', encoding='utf-8') as file:
    input = [int(i.strip()) for i in file]


# -- PART 1 --
combinatorials = itertools.combinations(set(input), 2)
for i in combinatorials:
    if sum(i) == 2020:
        print(i[0] * i[1])


# -- PART 2 --
combinatorials = itertools.combinations(set(input), 3)
for i in combinatorials:
    if sum(i) == 2020:
        print(i[0] * i[1] * i[2])
