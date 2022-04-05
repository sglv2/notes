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


class M1:
    info = 'example'

    def __init__(self, x):
        self.x = x

    @staticmethod
    def square(n):
        return n ** 2

    def get_info(self):
        return self.info

    @classmethod
    def print_info(cls):
        print(f'cls.info={cls.info}')
        print(f'cls.get_info()={cls.get_info(cls)}')


print(M1.square(2))
M1.increment_by_1()