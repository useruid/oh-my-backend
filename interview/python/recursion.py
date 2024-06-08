def rec(x):
    if x < 4:
        print(x)
        rec(x + 1)
        print(x)


rec(1)


def factorial(x):
    if x == 1:
        return 1
    return factorial(x - 1) * x


factorial(4)


def fibonacchi(n):
    print(n)
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacchi(n - 1) + fibonacchi(n - 2)


fibonacchi(7)
