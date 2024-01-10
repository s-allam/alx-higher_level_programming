#!/usr/bin/python3
def uniq_add(my_list=[]):
    mYset = set(my_list)
    count = 0
    for i  in mYset:
        count +=i
    return count
