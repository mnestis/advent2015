#!/usr/bin/python

def hits_basement(input_string):
    floor = 0
    position = 1

    for char in input_string:
        floor += 1 if char == "(" else -1
        if floor == -1:
            return position
        position += 1

if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print hits_basement(input_string)
