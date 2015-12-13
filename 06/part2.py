#!/usr/bin/python

import numpy
import re

def lots_of_lights(input_string):
    
    array = numpy.zeros((1000,1000), dtype=numpy.int16)
    
    coords = re.compile("(\d{1,3}),(\d{1,3})")
    
    for row in input_string.split("\n"):
        if row == "":
            continue

        inst_coords = coords.findall(row)

        section = array[ int(inst_coords[0][0]) : int(inst_coords[1][0])+1 , int(inst_coords[0][1]) : int(inst_coords[1][1])+1 ]

        if row.startswith("turn on"):
            section += numpy.ones(section.shape)
        elif row.startswith("turn off"):
            section -= numpy.ones(section.shape)
            section = numpy.maximum(section, numpy.zeros(section.shape))
        elif row.startswith("toggle"):
            section += 2*numpy.ones(section.shape)
            
        array[ int(inst_coords[0][0]) : int(inst_coords[1][0])+1 , int(inst_coords[0][1]) : int(inst_coords[1][1])+1 ] = section
    
    return numpy.sum(array)

if __name__=="__main__":

    input_string = open("input.txt").read()

    print lots_of_lights(input_string)
