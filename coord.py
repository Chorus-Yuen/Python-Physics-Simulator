from dataclasses import dataclass
from math import sqrt


@dataclass
class Coord:
    x: int
    y: int

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Coord):
            return Coord(self.x * other.x, self.y * other.y)
        else:
            return Coord(self.x * other, self.y * other)

    def div(self, other):
        return Coord(self.x / other, self.y / other)

    def pyth(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def mod(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def gradient(self, other):
        if self.x == other.x:
            return float('inf')
        return (self.y - other.y) * 10 / (self.x - other.x)

    def direction(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def cross(self, other): # Return scalar
        return self.x * other.y - self.y * other.x