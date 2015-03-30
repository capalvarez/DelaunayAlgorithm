__author__ = 'cata'

from random import randint
from Point import Point2D
from Triangle import Triangle

def randomPoints(number,low,high):
    points = []

    for i in range(0,number):
        points = points + [Point2D(randint(low,high),randint(low,high))]

    return points

def randomTriangles(number,low,high):
    triangles = []

    for i in range(0,number):
        triangles = triangles + [Triangle(Point2D(randint(low,high),randint(low,high)),
                                          Point2D(randint(low,high),randint(low,high)),
                                          Point2D(randint(low,high),randint(low,high)))]

    return triangles



if __name__ == '__main__':
    points = randomPoints(5,10,20)

    for i in range(0,len(points)):
        print points[i]