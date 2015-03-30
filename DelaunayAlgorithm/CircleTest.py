__author__ = 'cata'

from Utilities import *

from Point import Point2D

def circleTest(a,b,c,d):
    #Decide si una triangulacion local es Delaunay o no; devuelve -1 si el punto d esta dentro del circulo (no cumple
    # condicion) o 1 si cumple

    p11 = abs(a.getX()) - abs(d.getX())
    p12 = abs(a.getY()) - abs(d.getY())
    p13 = (abs(a.getX()) - abs(d.getX()))**2 + (abs(a.getY()) - abs(d.getY()))**2

    p21 = abs(b.getX()) - abs(d.getX())
    p22 = abs(b.getY()) - abs(d.getY())
    p23 = (abs(b.getX()) - abs(d.getX()))**2 + (abs(b.getY()) - abs(d.getY()))**2

    p31 = abs(c.getX()) - abs(d.getX())
    p32 = abs(c.getY()) - abs(d.getY())
    p33 = (abs(c.getX()) - abs(d.getX()))**2 + (abs(c.getY()) - abs(d.getY()))**2

    return p11*(p22*p33 - p32*p23) - p21*(p12*p33 - p32*p13) + p31*(p12*p23 - p13*p22)


def CClockwise(pA,pB,pC):
    return (pB.getX() - pA.getX())*(pC.getY() - pA.getY()) - (pC.getX() - pA.getX())*(pB.getY() - pA.getY()) > 0


if __name__ == '__main__':
    points = [Point2D(100,100),Point2D(200,100),Point2D(100,200),Point2D(150,150)]
    print circleTest(points[0],points[2],points[1],points[3])
