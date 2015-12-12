#!/usr/bin/python

import hashlib

def advent_coin_hash(input_string):
    
    x = 0
    hash = hashlib.md5(input_string + str(x)).hexdigest()

    while hash[:5] != "00000":
        x += 1
        hash = hashlib.md5(input_string + str(x)).hexdigest()

    return x

if __name__=="__main__":

    input_string = "ckczppom"

    print advent_coin_hash(input_string)
