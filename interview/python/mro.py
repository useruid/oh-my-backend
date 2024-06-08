class A:
    @classmethod
    def say_hello(cls):
        print('A')
    pass


class B(A):
    @classmethod
    def say_hi(cls):
        print('B')
    pass



class C(A):
    @classmethod
    def say_hi(cls):
        print('c')
    pass


class D(B, C):
    pass

D.say_hello()