#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit (1)
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.arv[3])
    match op:
        case "+":
            ans = add(a ,b)
        case "-":
            ans = sub(a, b)
        case "*":
            ans = mul(a, b)
        case "/":
            ans = div(a, b)
        case _:
            print("Unknown operator. Available operators: +, -, *, and /")
            sys.exit (1)
    print("{} {} {} = {}".format(a, op, b, ans))
            


