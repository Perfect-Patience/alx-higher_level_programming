#!/usr/bin/python3
from asyncio.windows_events import NULL
from contextlib import nullcontext
from queue import Empty
from requests import NullHandler


def best_score(a_dictionary):
    if a_dictionary is None or  not a_dictionary:
        return None
    list1 = list(a_dictionary)
    max = list1[0]
    for i, j in a_dictionary.items():
        if j > a_dictionary[max]:
            max = i
    return max
