#!/usr/bin/python

import re

def reindeer_chem(input_string):

    subs_re = re.compile("(\w+) => (\w+)")

    rules = {}
    back_rules = {}
    medicine = ""

    for rule in input_string.split("\n"):
        subs = subs_re.match(rule)

        if subs is not None:
            groups = subs.groups()

            if groups[0] not in rules:
                rules[groups[0]] = [groups[1]]
            else:
                rules[groups[0]].append(groups[1])

            if groups[1] not in back_rules:
                back_rules[groups[1]] = groups[0]
            else:
                raise NotImplementedError("My algorithm won't work with this...")
        else:
            if rule == "":
                continue
            else:
                medicine = rule
    

    steps = 0 

    back_values = sorted(back_rules.keys(), key=lambda x: len(x), reverse=True)

    while True:
        for value in back_values:
            if value in medicine:
                medicine = medicine.replace(value, back_rules[value], 1)
                steps += 1
                break
        else:
            break

    return steps
    

if __name__=="__main__":

    input_string = open("input.txt").read()

    print reindeer_chem(input_string)
