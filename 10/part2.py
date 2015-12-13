#!/usr/bin/python

import re

def load_conway_table():
    input_string = open("conway.txt").read()

    pattern = re.compile("(\d+) (\w+) (((\w+) )+)(\d+) (\d+)")

    table = {}

    for row in input_string.split("\n"):
        if row == "":
            continue
        pattern_match = pattern.match(row).groups()
        table[pattern_match[1]] = (pattern_match[2].split(" ")[:-1], len(pattern_match[-2]))

    return table

def look_and_say(input_string, conway_table):
    new_string = []

    for item in input_string:
        new_string.extend(conway_table[item][0])

    return new_string

if __name__=="__main__":
    
    input_string = ["Po"]

    conway_table = load_conway_table()

    for i in range(50):
        input_string = look_and_say(input_string, conway_table)

    length = 0
    for item in input_string:
        length += conway_table[item][1]

    print length
