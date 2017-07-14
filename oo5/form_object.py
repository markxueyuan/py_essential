# when to consider to define a class?
# illustration

import math

square =[(1,1), (1,2), (2,2), (2,1)] # a list of tuples

## non oo codes
## oo is about combination of data and behavior
## corresponds to data structure and function in
## general way of programming

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    return perimeter

def main():
    print(perimeter(square))

## change the above codes into oo paradigm

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self, p2):
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)


class Polygon:
    def __init__(self):
        self.vertices = []

    def add_point(self, point):
        self.vertices.append((point)) # [this extra parenthesis makes no change]

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter


def main2():
    square = Polygon()
    square.add_point(Point(1,1))
    square.add_point(Point(1,2))
    square.add_point(Point(2,2))
    square.add_point(Point(2,1))
    print(square.perimeter())


class EasyPolygon(Polygon):
    def __init__(self, points=None):
        points = points if points else []  # techniques should be grasped
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point) # remember this
            self.vertices.append(point)


def main3():
    square = EasyPolygon(points=[(1,1), (1,2), (2,2), (2,1)])
    print(square.perimeter())


if __name__ == "__main__":
    main3()


