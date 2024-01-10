#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp_ls = my_list[:]
    if 0 <= idx < len(my_list):
        tmp_ls[idx] = element
        return(tmp_ls)
    return(my_list)
