numbers = [1,2,3,4,5]
squared_numbers = (number**2 for number in numbers)
set_of_number = {1,2,3,4,5}

4 in squared_numbers

fruits_amount = {'apples': 2, 'bananas': 5}

x, y = fruits_amount

unordered_numbers = {1,2,3}


next(iter(numbers))

numbers = [1,2,3,4,5]
a,b, *rest = numbers


def custom_range(number):
    index = 0
    while index < number:
        yield index
        index += 1


my_range = custom_range(10)

for i in my_range:
    print(i)



# генераторы - это тоже итераторы
class InfiniteSquaring:
    """Класс обеспечивает бесконечное последовательное возведение в квадрат заданного числа."""
    def __init__(self, initial_number):
        # Здесь хранится промежуточное значение
        self.number_to_square = initial_number

    def __next__(self):
        # Здесь мы обновляем значение и возвращаем результат
        self.number_to_square = self.number_to_square ** 2
        return self.number_to_square

    def __iter__(self):
        """Этот метод позволяет при передаче объекта функции iter возвращать самого себя, тем самым в точности реализуя протокол итератора."""
        return self

my_iter = InfiniteSquaring(10)

iter(my_iter) is my_iter

# генератор - это итератор, элементы которого можно обойти только 1 раз
def ez_gen(x):
    yield x


gen = ez_gen(10)

while True:
    try:
        res = next(gen)
    except StopIteration:
        print('stopped')
        break
    else:
        print(res)
    finally:
        print('finished iteration')

lst = [1, 2, 3]
iter_lst = iter(lst)

for i in iter_lst:
    print(i)

def generator_lst(lst):
    '''тут генератор по сути является итератором
    то есть мы можем использовать next без промежуточного создания iter(lst)
    '''
    for el in lst:
        yield el

gen_lst = generator_lst(lst)

for i in gen_lst:
    print(i)

for i in gen_lst:
    print(i)

# где полезно
c = range(1000000000000)

for _ in c:
    print(_)


class MyNumbers:
    def __init__(self, initial_point):
        self.initial_point = initial_point

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.initial_point
        self.initial_point += 1
        return tmp


myclass = MyNumbers(10)
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


def my_fibo(n):
    return 1 if n == 1 else my_fibo(n - 1) + my_fibo(n - 2)



my_fibo(10)


class MyIter:
    def __init__(self, max_value):
        self.max_value = max_value
        self._current_value = 0

    def __iter__(self):
        return self

    @property
    def current_value(self):
        if self._current_value < self.max_value:
            current_value = self._current_value
            self._current_value += 1
            return current_value
        else:
            raise StopIteration

    def __next__(self):
        return self.current_value


