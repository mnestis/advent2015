#!/usr/bin/python

import re

def reindeer_games(input_string):
    reindeer_re = re.compile("(\w+)[^\d]+(\d+)[^\d]+(\d+)[^\d]+(\d+)")

    reindeer = {}

    end_time = 2503

    for row in input_string.split("\n"):
        if row == "":
            continue

        groups = reindeer_re.match(row).groups()
        reindeer[groups[0]] = {"distance": 0,"speed": int(groups[1]), "runtime": int(groups[2]), "sleeptime": int(groups[3])}
    
    for second in range(end_time):
        for deer in reindeer:

            deer = reindeer[deer]
            if second % (deer["runtime"]+deer["sleeptime"]) < deer["runtime"]:
                deer["distance"] += deer["speed"]

    return sorted(reindeer.items(), key=lambda deer: deer[1]["distance"])[-1][1]["distance"]

if __name__=="__main__":

    input_string = open("input.txt").read()

    print reindeer_games(input_string)
