#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv)
    print("{} arguments:".format(n - 1))
    for i in range(1, n):
        print("{}: {}".format(i, argv[i]))
