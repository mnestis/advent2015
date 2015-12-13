#!/usr/bin/python

import re

def calculate_file_size(input_string):
    
    code_size = 0
    actual_size = 0
    
    for row in input_string.split("\n"):
        if row == "":
            continue

        actual_size += len(row)
        row = row.replace("\\", "\\\\")
        row = row.replace("\"", "\\\"")
        row = "\"" + row + "\""
        code_size += len(row)

    return code_size - actual_size

if __name__=="__main__":
    
    input_string = open("input.txt").read()

    print calculate_file_size(input_string)
