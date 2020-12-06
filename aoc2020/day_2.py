#!/usr/bin/python3

import itertools

counter_1  = 0 #PART 1
counter_2  = 0 #PART 2

# -- Open File --
file_input = 'input.txt'

with open(file_input, 'r', encoding='utf-8') as file:
    for i in file:
        input           = i.split(': ')
        password        = input[-1]
        validator_txt   = input[0].split(' ')

        occurence_range = validator_txt[0].split('-')
        letter          = validator_txt[-1]
        password_count  = password.count(letter)


        # -- PART 1 --
        if password_count >= int(occurence_range[0]) and password_count <= int(occurence_range[1]):
            counter_1 += 1


        # -- PART 2 --
        password_position = [password[int(occurence_range[0])-1], password[int(occurence_range[1])-1]]
        if password_position.count(letter) == 1:
            counter_2 += 1


print('PART 1: ', counter_1) #PART 1
print('PART 2: ', counter_2) #PART 2
