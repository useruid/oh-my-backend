"""generators_3 - run in terminal"""


def generator(x):
    while True:
        x = yield x + 1


g = generator(5)

g.send(None)

g.send(10)

##############################################


def grep(pattern):
    print("Looking for {}".format(pattern))
    while True:
        line = (yield)
        if pattern in line:
            print(line)


g = grep("python")
next(g)
g.send("Yeah, but no, but yeah, but no")
g.send("A series of tubes")
g.send("python generators rock!")
