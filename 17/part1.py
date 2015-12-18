#!/usr/bin/python

import itertools

def find_container_combinations(input_string, litres):

    containers = []

    for row in input_string.split("\n"):
        if row == "":
            continue

        containers.append(int(row))

    containers.sort(reverse=True)

    return count_possible_combinations(containers, litres)

def count_possible_combinations(containers, goal):
    
    possible_combs = 0

    if goal <= 0:
        raise Exception("Goal cannot be less than or equal to 0")

    if containers == []:
        raise Exception("Containers should not be empty list.")

    if sum(containers) < goal:
        return 0

    if containers[0] == goal:
        next_subset = containers[containers.count(goal):]
        return containers.count(goal) + (count_possible_combinations(next_subset, goal) if next_subset != [] else 0)
    
    if containers[0] > goal:
        possible_combs += count_possible_combinations(containers[1:], goal)
    else:
        possible_combs += count_possible_combinations(containers[1:], goal - containers[0])
        possible_combs += count_possible_combinations(containers[1:], goal)

    return possible_combs

if __name__=="__main__":
    
    input_filename = "input.txt"
    litres = 150

    input_string = open(input_filename).read()

    print find_container_combinations(input_string, litres)
