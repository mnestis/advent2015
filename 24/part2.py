#!/usr/bin/python

import itertools

def find_ideal_arrangement(input_string):
    parcels = []
    
    for line in input_string.split("\n"):
        if line == "":
            continue

        parcels.append(int(line))

    weight_in_each_section = sum(parcels) / 4.0

    smallest_qe = 100000000000000
    for x in range(1,5):
        for comb in itertools.combinations(parcels, x):
            if sum(comb) == weight_in_each_section:
                qe = reduce(lambda a, b: a*b, comb)
                if qe < smallest_qe:
                    smallest_qe = qe

    return smallest_qe


if __name__=="__main__":

    input_string = open("input.txt").read()

    print find_ideal_arrangement(input_string)
