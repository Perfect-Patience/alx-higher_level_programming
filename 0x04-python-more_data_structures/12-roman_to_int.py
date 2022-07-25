#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    res = 0
    base_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M': 1000}
    roman_string = roman_string.upper()
    list1 = []
    for i in roman_string:
        for j , r in base_numerals.items():
            if i == j:
                list1.append(r)
    if list1 == sorted(list1, reverse=True):
        for i in list1:
            res += i
    else:
        for i in range(len(list1) - 1):
            if list1[i] < list1[i + 1]:
                res += (list1[i + 1] - list1[i])
            else:
                res += list1[i]
    return res
