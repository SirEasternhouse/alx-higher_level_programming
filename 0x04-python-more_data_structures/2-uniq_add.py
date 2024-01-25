#!/usr/bin/python3
def uniq_add(my_list=[]):
    tot = 0
    seen_elements = set()
    for i in my_list:
        if i and i not in seen_elements:
            tot += i
            seen_elements.add(i)
    return tot
