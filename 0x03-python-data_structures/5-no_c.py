#!/usr/bin/python3
def no_c(my_string):
    j = 0
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        new_string[j] = my_string[i]
        j += 1
    return my_string
