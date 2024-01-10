#!/usr/bin/python3
def search_replace(my_list, search, replace):
    arr = []
    for i in my_list :
        if i == search:
            arr.append(replace)
        else:
            arr.append(i)
    return i
