#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv)
    sum_arg = 0
    if n > 1:
        for i in range(1, n):
            sum_arg += int(argv[i])
    print(sum_arg)
