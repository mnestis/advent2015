#!/usr/bin/python

import numpy as np
import re
import itertools

def animated_lights(input_string):

    other_chars = re.compile("[^#\.]")

    lights = []
    for row in input_string.split("\n"):
        if row == "":
            continue

        row = other_chars.sub("", row)
        row = row.replace("#", "1")
        row = row.replace(".", "0")

        lights.append(map(lambda x: int(x), row))

    lights = np.array(lights, dtype=int)

    for i in range(100):
        lights = step_lights(lights)

    return np.sum(lights)

def step_lights(lights):

    next_lights = np.empty(lights.shape, dtype=int)

    for i, j in itertools.product(range(lights.shape[0]), range(lights.shape[1])):

        x0 = max(i-1, 0)
        x1 = min(i+2, lights.shape[0])
        y0 = max(j-1, 0)
        y1 = min(j+2, lights.shape[1])

        neighbourhood = np.sum(lights[x0:x1, y0:y1])
        if lights[i,j] == 1:
            next_lights[i,j] = 1 if neighbourhood == 3 or neighbourhood == 4 else 0
        else:
            next_lights[i,j] = 1 if neighbourhood == 3 else 0

    return next_lights

if __name__=="__main__":

    input_string = open("input.txt").read()

    print animated_lights(input_string)
