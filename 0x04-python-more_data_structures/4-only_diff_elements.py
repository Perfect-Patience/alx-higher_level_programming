#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list1 = list(set_1.difference(set_2))
    list1.extend(list(set_2.difference(set_1)))
    return list1
