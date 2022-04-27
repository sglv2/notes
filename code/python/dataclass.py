from dataclasses import dataclass


@dataclass
# (frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        """"Add 2 instances using +"""
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        """"Substract 2 instances using -"""
        return Point(
            self.x - other.x,
            self.y - other.y
        )


x = Point(1, 1)
y = Point(3, 3)
z = x + y
print(z)

print(f'{isinstance(x, Point)=}')