#!/usr/bin/python

def count_visited_houses(input_string):
    
    santas = [(0,0),(0,0)]

    visited_houses = [(0,0)]
    
    for index, char in enumerate(input_string):
        s = index % 2
        santas[s] = calc_new_coords(char, santas[s])
        if santas[s] not in visited_houses:
            visited_houses.append(santas[s])

    return len(visited_houses)

def calc_new_coords(char, start_coords):
    if char == "<":
        return (start_coords[0]-1, start_coords[1])
    elif char == ">":
        return (start_coords[0]+1, start_coords[1])
    elif char == "^":
        return (start_coords[0], start_coords[1]+1)
    elif char == "v":
        return (start_coords[0], start_coords[1]-1)
    else:
        raise Exception("Invalid direction received...")

if __name__=="__main__":

    input_string = open("input.txt").read()

    print count_visited_houses(input_string)
