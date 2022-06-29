#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    Last_digit = number % 10
    print(Last_digit, end="")
    return Last_digit
