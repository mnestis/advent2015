#!/usr/bin/python

import re

two_diff_nonoverlapping_pairs = re.compile("(?P<char>\w)(?P=char).(?P<char2>\w)(?P=char2)")

def find_new_password(old_password):
    
    new_password = next_password(old_password)
    while not check_password_validity(new_password):
        new_password = next_password(new_password)

    return new_password

def next_password(old_password):
    if old_password[-1] == "z":
        return next_password(old_password[:-1]) + "a"

    else:
        return old_password[:-1] + chr(ord(old_password[-1])+1)

def check_password_validity(password):
    
    for i in range(len(password)-2):
        if ord(password[i]) + 2 == ord(password[i+1]) + 1 == ord(password[i+2]):
            break
    else:
        return False

    if "i" in password or "o" in password or "l" in password:
        return False

    match_obj = two_diff_nonoverlapping_pairs.search(password)
    if match_obj is None:
        return False

    if match_obj.groups()[0] == match_obj.groups()[1]:
        return False

    return True

if __name__=="__main__":

    original_password = "vzbxkghb"

    print find_new_password(original_password)
