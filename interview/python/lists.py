a = [1, 2, 3, 4, 5]
b = [5, 6, 7]


a.extend(a)
a + b
a += b
a.append(iter([*a]))


my_tuple = tuple([1, 2, 3, ['a', 'b']])

my_tuple[-1].append('3')

my_dct = {my_tuple: 10}

my_dct[my_tuple]