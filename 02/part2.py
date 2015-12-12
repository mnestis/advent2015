#!/usr/bin/python

def ribbon_needed(input_string):

    ribbon_needed = 0
    
    rows = input_string.split("\n")
    for row in rows:
        if row == "":
            continue

        sides = sorted(map(lambda x: int(x), row.split("x")))

        ribbon_needed += 2*sides[0] + 2*sides[1] + sides[0]*sides[1]*sides[2]

    return ribbon_needed

        

if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print ribbon_needed(input_string)
