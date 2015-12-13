#!/usr/bin/python

import re

def look_and_say(input_string):
    
    conseq = re.compile("((?P<char>\w)(?P=char)*)")

    conseq_groups = conseq.findall(input_string)

    list_of_chars = map(lambda a: str(len(a[0])) + a[1], conseq_groups)
    combined_str = reduce(lambda a, b: a+b, list_of_chars)
    return combined_str

if __name__=="__main__":
    
    input_string = "1113222113"

    for i in range(40):
        input_string = look_and_say(input_string)

    print len(input_string)
