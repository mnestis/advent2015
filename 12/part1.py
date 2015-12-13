#!/usr/bin/python

import re

def find_all_numbers(input_string):
    return map(lambda a: int(a), re.findall("(-?\d+)", input_string, re.MULTILINE))
    

def sum_all_numbers(input_string):
    return sum(find_all_numbers(input_string))

if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print sum_all_numbers(input_string)
    
