# Methods which have names starting with __ are called "dunder" methods and represent special behavior
# Methods with names starting with _ represent private methods, however Python will allow these to be called anyway
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_ten(self):
        self.x += 10
        self.y += 10


c1 = Coord(10, 20)
c1.add_ten()
print(f'{c1.x} {c1.y}')


class NewCoord(Coord):
    def __init__(self, x, y):
        super().__init__(x, y)

    def multiply_by_ten(self):
        self.x *= 10
        self.y *= 10


c2 = NewCoord(10, 20)
c2.multiply_by_ten()
print(f'{c2.x} {c2.y}')


class Example:
    info = 'some info'

    def __init__(self, x):
        self.x = x

    @staticmethod
    def square(n):
        return n ** 2

    def get_info(self):
        return self.info

    # The class method will change the value of 'info' for all instances
    # A class method is a method that is bound to the class and not the object of the class
    @classmethod
    def set_info(cls, info):
        cls.info = info


print(Example.square(2))
m1 = Example(1)
m2 = Example(2)
m1.set_info('new info')
print(m1.get_info())
print(m2.get_info())


class Natural:

    def __init__(self, num):
        self._num = num

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, new_num):
        if new_num > 0 and isinstance(new_num, int):
            self._num = new_num
        else:
            print(f'{new_num} is not valid')

    @num.deleter
    def num(self):
        del self._num


n = Natural(1)
print(f'{n.num=}')
# The setter will be called
n.num = -1
