#!/usr/bin/python

import itertools
import re

def calculate_optimum_happiness(input_string):
    
    happy_re = re.compile("(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).")

    guests = {}

    for row in input_string.split("\n"):
        if row == "":
            continue

        groups = happy_re.match(row).groups()
        
        if groups[0] not in guests:
            guests[groups[0]] = {}

        guests[groups[0]][groups[-1]] = int(groups[2]) if groups[1]=="gain" else -int(groups[2])

    greatest_happiness_achieved = 0
    for perm in itertools.permutations(guests.keys()):
        partners = zip(perm[:-1], perm[1:])
        partners.append((perm[0],perm[-1]))

        cumulative_happiness = 0
        for p in partners:
            cumulative_happiness += guests[p[0]][p[1]] + guests[p[1]][p[0]]

        if cumulative_happiness > greatest_happiness_achieved:
            greatest_happiness_achieved = cumulative_happiness

    return greatest_happiness_achieved

if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print calculate_optimum_happiness(input_string)
