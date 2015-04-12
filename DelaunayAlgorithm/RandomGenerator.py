__author__ = 'cata'

from random import randint
from Point import Point2D

def randomPoints(number,low,high):
    points = []

    for i in range(0,number):
        points = points + [Point2D(randint(low,high),randint(low,high))]

    return points
