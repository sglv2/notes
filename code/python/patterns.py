# Singleton
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, new_num):
        self._num = new_num


s1 = Singleton()
s2 = Singleton()
s1.num = 1
print(f'{s2.num=}')

# Builder

from abc import ABC, abstractmethod


class abstractObj(ABC):
    @abstractmethod
    def addP1(self):
        pass

    @abstractmethod
    def addP2(self):
        pass

    @abstractmethod
    def show(self):
        pass


class FirstObj(abstractObj):
    def __init__(self):
        self.p1 = 0
        self.p2 = 0

    def addP1(self, p1):
        self.p1 = p1

    def addP2(self, p2):
        self.p1 = p2

    def show(self):
        print(f'{self.p1=} {self.p2=}')


class SecondObj(abstractObj):
    def __init__(self):
        self.p1 = 1
        self.p2 = 1

    def addP1(self, p1):
        self.p1 = p1 * 2

    def addP2(self, p2):
        self.p1 = p2 * 2

    def show(self):
        print(f'{self.p1=} {self.p2=}')

o1: abstractObj = FirstObj()
o1.addP1(10)
o1.show()

o2: abstractObj = SecondObj()
o2.addP1(10)
o2.show()