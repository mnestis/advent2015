#!/usr/bin/python

import itertools

def find_container_combinations(input_string, litres):

    containers = []

    for row in input_string.split("\n"):
        if row == "":
            continue

        containers.append(int(row))

    containers.sort(reverse=True)

    combinations = count_possible_combinations(containers, litres)
    min_length = min(map(lambda x: len(x), combinations))
    
    return len(filter(lambda x: len(x)==min_length, combinations))

def count_possible_combinations(containers, goal):
        
    if goal <= 0:
        raise Exception("Goal cannot be less than or equal to 0")

    if containers == []:
        raise Exception("Containers should not be empty list.")

    if sum(containers) < goal:
        return []

    if containers[0] == goal:
        next_subset = containers[containers.count(goal):]
        
        subset_combinations = []
        
        if next_subset != []:
            subset_combinations.extend(count_possible_combinations(next_subset, goal))
            
        for x in range(containers.count(goal)):
            subset_combinations.append([goal])
    
        return subset_combinations

    possible_combs = []
    if containers[0] > goal:
        possible_combs.extend(count_possible_combinations(containers[1:], goal))
    else:
        possible_combs.extend([ [containers[0]] + comb for comb in count_possible_combinations(containers[1:], goal - containers[0])])
        possible_combs.extend(count_possible_combinations(containers[1:], goal))

    return possible_combs

if __name__=="__main__":
    
    input_filename = "input.txt"
    litres = 150

    input_string = open(input_filename).read()

    print find_container_combinations(input_string, litres)
