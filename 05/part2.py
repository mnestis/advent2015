#!/usr/bin/python

import re

def count_nice_strings(input_string):
    
    nice = 0

    rule1 = re.compile("(?P<chars>\w\w).*(?P=chars)")
    rule2 = re.compile("(?P<char>\w)\w(?P=char)")

    for string in input_string.split("\n"):
        if string == "":
            continue

        if len(rule1.findall(string)) > 0 and len(rule2.findall(string)) > 0:
            nice += 1

    return nice


if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print count_nice_strings(input_string)
