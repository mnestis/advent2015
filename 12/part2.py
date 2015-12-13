#!/usr/bin/python

import json

def process_json_file(input_filename):

    json_obj = json.load(open(input_filename))

    return process_obj(json_obj)

def process_obj(obj):
    
    running_total = 0

    for key in obj:
        if obj[key] == "red":
            break
    else:
        for key in obj:
            if isinstance(obj[key], int):
                running_total += obj[key]
            elif isinstance(obj[key], list):
                running_total += process_list(obj[key])
            elif isinstance(obj[key], unicode):
                pass
            else:
                running_total += process_obj(obj[key])

    return running_total

def process_list(lst):

    running_total = 0

    for item in lst:
        if isinstance(item, int):
            running_total += item
        elif isinstance(item, list):
            running_total += process_list(item)
        elif isinstance(item, unicode):
            pass
        else:
            running_total += process_obj(item)

    return running_total
    

if __name__=="__main__":
    
    print process_json_file("input.txt")
    
