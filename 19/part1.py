#!/usr/bin/python

import re

def reindeer_chem(input_string):

    subs_re = re.compile("(\w+) => (\w+)")

    rules = {}
    medicine = ""

    for rule in input_string.split("\n"):
        subs = subs_re.match(rule)

        if subs is not None:
            groups = subs.groups()

            if groups[0] not in rules:
                rules[groups[0]] = [groups[1]]
            else:
                rules[groups[0]].append(groups[1])
        else:
            if rule == "":
                continue
            else:
                medicine = rule
    

    evolutions = {}

    for elem, repls in rules.items():
        
        pos = 0

        while True:
            elem_re = re.compile(elem)
            result = elem_re.search(medicine, pos)

            if result is None:
                break

            for repl in repls:
                evolution = medicine[0:result.start()] + repl + medicine[result.end():]
                if evolution in evolutions:
                    evolutions[evolution] += 1
                else:
                    evolutions[evolution] = 1

            pos = result.end()

    return len(evolutions.keys())
    

if __name__=="__main__":

    input_string = open("input.txt").read()

    print reindeer_chem(input_string)
