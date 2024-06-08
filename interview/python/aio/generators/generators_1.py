"""generators_1 - run in terminal"""

a = (i**2 for i in range(1, 5))

next(a)

for i in a:
    print(i)


def countdown(n):
    while n > 0:
        yield n
        n -= 1


for i in countdown(5):
    print(i)


