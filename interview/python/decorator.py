from functools import wraps
from typing import Callable


def my_func():
    print('my function workse')


def hello_goodbye(func: Callable):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        print('hello')
        result = func(*args, **kwargs)
        print('goodbye')
        return result
    return wrapper

my_func()


@hello_goodbye
def my_func_wrapped():
    my_func()

my_func_wrapped()

print(my_func_wrapped)


def outer(n):
    def hello_goodbye(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'hello {n} times')
            result = func(*args, **kwargs)
            print(f'goodbye {n} times')
            return result
        return wrapper
    return hello_goodbye


@outer(3)
def my_func_wrapped_params():
    my_func()


my_outer_3 = outer(3)

my_func_wrapped = my_outer_3(my_func)

my_func_wrapped_params()


my_func_wrapped()


def hello_times(n):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            print('start')
            result = func(*args, **kwargs)
            print('end')
            return result
        return wrapper
    return decorator
