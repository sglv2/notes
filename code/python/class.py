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