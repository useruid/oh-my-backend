from abc import ABC, abstractmethod, ABCMeta


# abstract
class Car(ABC):

    @abstractmethod
    def start_engine(self):
        ...


class Truck(Car):
    def __init__(self):
        pass

    def start_engine(self):
        print('engine started')



my_truck = Truck()

my_truck.start_engine()

# meta
# если хотим чтобы и абстрактный можно было делать
class OneMeta(ABCMeta):
    pass


# этот уже не будет абстрактный классом
class TwoMeta(type):
    def __new__(msc, name, bases, attrs):
        pass
