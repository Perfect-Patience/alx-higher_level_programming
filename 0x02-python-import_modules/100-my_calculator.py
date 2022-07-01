#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op == "+":
        ans = add(a, b)
    elif op == "-":
        ans = sub(a, b)
    elif op == "*":
        ans = mul(a, b)
    elif op == "/":
        if b == 0:
            exit()
        ans = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, op, b, ans))
