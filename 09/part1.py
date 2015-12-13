#!/usr/bin/python

import itertools
import re
import numpy

def shortest_distance(input_string):
    
    distance_re = re.compile("(\w+) to (\w+) = (\d+)")

    cities = {}

    for row in input_string.split("\n"):
        if row == "":
            continue
        
        start, end, dist = distance_re.match(row).groups()
        if start in cities:
            cities[start][end] = int(dist)
        else:
            cities[start] = {end : int(dist)}

        if end in cities:
            cities[end][start] = int(dist)
        else:
            cities[end] = {start : int(dist)}

    shortest_distance = 1000000000
    for perm in itertools.permutations(cities.keys()):
        total_distance = sum(map(lambda pair: cities[pair[0]][pair[1]], zip(perm[:-1],perm[1:])))
        if total_distance < shortest_distance:
            shortest_distance = total_distance
        
    return shortest_distance

if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print shortest_distance(input_string)
