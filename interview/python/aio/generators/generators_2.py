def f_gen():
    n = 1
    while True:
        yield n**2
        n += 1


generator1 = f_gen()
generator2 = f_gen()


# for i in generator1:
#     print(i)
#     if i > 10:
#         generator1.close()

for i in generator2:
    print(i)
    if i > 20:
        generator2.throw(Exception("Плохо!"))
