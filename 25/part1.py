#!/usr/bin/python

def calculate_code(x, y):

    number = 20151125

    for x in range(1, sum(range(1, x + y - 1)) + x):
        number = (number * 252533) % 33554393

    return number

if __name__=="__main__":
    
    x = 3029
    y = 2947

    print calculate_code(x, y)
