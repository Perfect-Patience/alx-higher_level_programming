#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    list1 = list(a_dictionary)
    max = list1[0]
    for i, j in a_dictionary.items():
        if j > a_dictionary[max]:
            max = i
    return max
