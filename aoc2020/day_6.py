#!/usr/bin/python3

import collections, itertools


# -- Open File --
file_input = 'input.txt'
with open(file_input, encoding='utf-8') as file:
    content = file.read()
    inputs  = content.split('\n\n')


# -- PART 1 --
counter_1 = 0
cleaned_1 = [i.replace('\n', '') for i in inputs]

for i in cleaned_1:
    counter_1 += len(set(i))

print(counter_1)


# -- PART 2 --
counter_2 = 0
cleaned_2 = [i.split() for i in inputs]

for x in cleaned_2:
    group_length    = len(x)
    group_answers   = list(itertools.chain.from_iterable(x))
    answers_counter = collections.Counter(group_answers)
    for y in answers_counter:
        if answers_counter[y] == group_length:
            counter_2 += 1

print(counter_2)
