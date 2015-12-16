#!/usr/bin/python

import re

def find_sue(input_string):
    sues = []

    sues_re = re.compile("Sue (\d+): (.+)") 

    features_of_sue = {"children": 3,
                       "cats": 7,
                       "samoyeds": 2,
                       "pomeranians": 3,
                       "akitas": 0,
                       "vizslas": 0,
                       "goldfish": 5,
                       "trees": 3,
                       "cars": 2,
                       "perfumes": 1}

    for row in input_string.split("\n"):
        if row == "":
            continue
        variables = sues_re.match(row).groups()[1]
        sue = {"number": sues_re.match(row).groups()[0]}
        for variable in variables.split(","):
            sue[variable.split(":")[0].strip()] = int(variable.split(":")[1].strip())

        for feature in sue:
            if feature == "number":
                continue
            if sue[feature] != features_of_sue[feature]:
                break
        else:
            sues.append(sue)
        

    return sues[0]["number"]
    

if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print find_sue(input_string)
