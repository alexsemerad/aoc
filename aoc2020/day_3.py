#!/usr/bin/python3

file_input = 'input.txt'

def arboreal_stop(right, down, file_input=file_input):
    with open(file_input, 'r') as file:
        track = [row.strip() for row in file]

    position = 0
    trees    = 0

    for i in range(0, len(track), down):
        if track[i][position] == '#':
            trees += 1

        position += right
        if position >= len(track[i]):
            position = abs(position - len(track[i]))

    return trees


r1d1 = arboreal_stop(1,1)
r3d1 = arboreal_stop(3,1)
r5d1 = arboreal_stop(5,1)
r7d1 = arboreal_stop(7,1)
r1d2 = arboreal_stop(1,2)

# -- PART 1 --
print(r3d1)

# -- PART 2 --
print(r1d1*r3d1*r5d1*r7d1*r1d2)
