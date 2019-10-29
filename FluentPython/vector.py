from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # String representation of the object for inspection
    # __str__ is for end user display, this is for inspection to recreate
    # if __str__ not defined fall back to __repr__
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # If not defined calls len to see if len returns 0
    # User classes are truthy if nothing is defined
    def __bool__(self):
        return bool(abs(self))

    # infix operators should return a new object
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
