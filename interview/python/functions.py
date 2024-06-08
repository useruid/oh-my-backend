# map
def my_func(x):
    return x ** 2


lst = [1, 2, 3, 4, 5]

mapped_lst = map(my_func, lst)

for i in mapped_lst:
    print(i)

# filter
def my_filter(x):
    return x % 2 == 0

filter_lst = filter(my_filter, lst)

for i in filter_lst:
    print(i)

# reduce
from functools import reduce
def my_reduce(x, y):
    return x * y

reduce(my_reduce, lst, 1)

