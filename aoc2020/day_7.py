#!/usr/bin/python3

import re

rules      = {}
file_input = 'input.txt'

with open(file_input, 'r', encoding='utf-8') as file:
    data = [i.strip() for i in file]

def parse_line(line):
    search_bag = re.search(parent_bag_regx, line)
    bag_key    = search_bag.group(1)
    bag_value  = re.findall(child_bags_regx, search_bag.group(2))
    return (bag_key, bag_value)

# -- Clean Input --
parent_bag_regx = '^(.*?) bags contain (.*?)$'
child_bags_regx = '(\d+) (\w+ \w+) bag'

for line in data:
    parsed = parse_line(line)
    key, value = parsed
    rules[key] = value


# -- PART 1 --
def bag_finder(target):
    bag_list = []
    for parent, child in rules.items():
        if any(sub_child == target for _, sub_child in child):
            bag_list.append(parent)
            bag_list += bag_finder(parent)
    return bag_list

print(len(set(bag_finder('shiny gold'))))


# -- PART 2 --
def bag_counter(target):
    counter = 0
    for parent, child in rules.items():
        if parent == target:
            if child:
                for sub_child in child:
                    counter += int(sub_child[0])
                    counter += int(sub_child[0]) * bag_counter(sub_child[1])
    return counter

print(bag_counter('shiny gold'))
