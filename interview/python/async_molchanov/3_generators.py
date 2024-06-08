def gen_inf():
    counter = 0
    while True:
        yield counter
        counter += 1


counter_inf = gen_inf()

next(counter_inf)


# event loop generators
def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1('george')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
