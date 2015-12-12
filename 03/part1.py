#!/usr/bin/python

def count_visited_houses(input_string):
    
    x, y = (0,0)

    visited_houses = [(0,0)]
    
    for char in input_string:
        if char == "<":
            x -= 1
        elif char == ">":
            x += 1
        elif char == "^":
            y += 1
        elif char == "v":
            y -= 1
        else:
            raise Exception("Invalid direction received...")

        if (x,y) not in visited_houses:
            visited_houses.append((x,y))

    return len(visited_houses)

if __name__=="__main__":

    input_string = open("input.txt").read()

    print count_visited_houses(input_string)
