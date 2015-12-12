#!/usr/bin/python

def final_floor(input_string):
    return input_string.count("(") - input_string.count(")")

if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print final_floor(input_string)



