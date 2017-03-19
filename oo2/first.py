import math

##
class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()

##
class Point:
    pass

p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

##
class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()

p.reset()

# which is equivalent to:

Point.reset(p)

# you must include self in your methods

class Point:
    def reset():
        pass

p = Point()

# 1
try:
    p.reset()
except  TypeError as e:
    print(e)

# 2
try:
    Point.reset(p)
except TypeError as e:
    print(e)

# 3
try:
    Point.reset()
except TypeError as e:
    print(e)

## multiple arguments

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2
            +
            (self.y - other_point.y) ** 2)

point1 = Point()
point2 = Point()
point1.reset()
point2.move(5,0)
point1.move(3,4)
point1.calculate_distance(point2)

## Initialization

# __sth__ will be treated by interpreter as a special case

class Point:
    def __init__(self, x, y):
        self.move(x, y)
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2
            +
            (self.y - other_point.y) ** 2)


point = Point(3,5)
point.x

## default arguments

class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2
            +
            (self.y - other_point.y) ** 2)


point = Point()
point.x
# But you still can freely assign value to the object
point.z = 4

## Constructor
class Point:
    def __new__(cls):
        pass

# __new__ construct an object, takes (at least) one argument, the class
# Since it is called before the objectis constructed,
        # so there is no self argument

## docstring
class Point:
    """
    Represents a point in two-dimensional geometric coordinates
    """
    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin.'''
        self.move(x, y)
    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y

    def reset(self):
        'Reset the point back to the geometric origin: 0, 0'
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second
        point passed as a parameter.
        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is
        returned as a float."""
        return math.sqrt(
            (self.x - other_point.x) ** 2
            +
            (self.y - other_point.y) ** 2)

help(Point)





