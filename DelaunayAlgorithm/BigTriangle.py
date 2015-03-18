__author__ = 'cata'
from Point import *
from Triangle import *

def bigTriangle(pointList,perc):
    #Encargado de devolver los tres puntos que forman el triangulo inicial del algoritmo
    (up,down,right,left) = findCorners(pointList)

    x1 = right.getX()*10
    y1 = up.getY()*10

    x2 = left.getX()*10
    y2 = down.getY()*10

    leftDownPoint = Point2D(x2 - (x1 - x2)*perc, y2)
    rightDownPoint = Point2D(x1 + (x1 - x2)*perc, y1)

    upXCoord = (rightDownPoint.getX() - leftDownPoint.getX())/2
    slope = (y1 - y2)/(upXCoord - rightDownPoint.getX())

    upPoint = Point2D(upXCoord, y1 + slope*(upXCoord - y1))

    return Triangle(upPoint,leftDownPoint,rightDownPoint)


def findCorners(pointList):
    #Encuentra las coordenadas mas a la izq, der, arriba y abajo (para encontrar el cuadrado cobertor de los puntos)
    up = pointList[0].getY()
    down = pointList[0].getY()
    right = pointList[0].getX()
    left = pointList[0].getX()

    for i in range(len(pointList)):
        if up < pointList[i].getY():
            up = pointList[i].getY()

        if down > pointList[i].getY():
            down = pointList[i].getY()

        if right < pointList[i].getX():
            right = pointList[i].getX()

        if left > pointList[i].getX():
            left = pointList[i].getX()

    return (up, down, right, left)

if __name__ == '__main__':
    points = [Point2D(0,0),Point2D(1,1)]
    print findCorners(points)


