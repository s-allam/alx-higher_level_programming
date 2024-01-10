#!/usr/bin/python3
def uniq_add(my_list=[]):
    mYset = set(my_list)
    count = mYset[0]
    for i  in mYset:
        if i != mYset[0]:
            count +=i
    return count
