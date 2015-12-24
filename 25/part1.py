#!/usr/bin/python

def do_thing(input_string):

    for line in input_string.split("\n"):
        if line == "":
            continue

        pass

if __name__=="__main__":

    input_string = open("input.txt").read()

    print do_thing(input_string)
