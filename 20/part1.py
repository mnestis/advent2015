#!/usr/bin/python

from math import sqrt

def elven_post(input):

    x = 0
    while True:
        if how_many_presents(x) > input:
            return x
        x += 1

def how_many_presents(house_number):

    divisors = set()

    for x in xrange(int(sqrt(house_number)), 0, -1):
        if house_number % x != 0:
            continue
        divisors.add(x)
        divisors.add(house_number/x)

    return sum(divisors) * 10

if __name__=="__main__":
    
    input = 34000000

    print elven_post(input)
