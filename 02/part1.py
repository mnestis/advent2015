#!/usr/bin/python

def paper_needed(input_string):

    paper_needed = 0
    
    rows = input_string.split("\n")
    for row in rows:
        if row == "":
            continue

        sides = sorted(map(lambda x: int(x), row.split("x")))

        paper_needed += 3*sides[0]*sides[1] + 2*sides[1]*sides[2] + 2*sides[0]*sides[2]

    return paper_needed

        

if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print paper_needed(input_string)
