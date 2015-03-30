__author__ = 'cata'
from Point import *
from FindTriangle import inTriangle
from Triangle import *
from RandomGenerator import randomPoints

def bigTriangle(pointList,perc):
    #Encargado de devolver los tres puntos que forman el triangulo inicial del algoritmo
    (up,down,right,left) = findCorners(pointList)

    x1 = right*1.5
    y1 = up*1.5

    x2 = left*0.6
    y2 = down*0.6

    leftUpPoint = Point2D(x2 - (x1 - x2)*perc, y1)
    rightUpPoint = Point2D(x1 + (x1 - x2)*perc, y1)

    upXCoord = (rightUpPoint.getX() - leftUpPoint.getX())/2
    slope = (y1 - y2)/(leftUpPoint.getX() - x2)

    downPoint = Point2D(upXCoord, y1 + slope*(upXCoord - leftUpPoint.getX()))

    return Triangle(downPoint,leftUpPoint,rightUpPoint)

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

def removeBigTriangle(bigTriangle,triangulation):
    #Ir punto a pu  nto del gran triangulo (?)
    return

if __name__ == '__main__':
    points = randomPoints(20,50,300)
    #points =[Point2D(100,100),Point2D(100,200),Point2D(200,200),Point2D(200,100)]

    window = Tk()
    frame = Frame(window)
    frame.pack()

    canvas = Canvas(window,width=600,height=400,bg="white")
    triangulation = [bigTriangle(points,0.5)]

    for i in range(0,len(points)):
    	points[i].draw(canvas)

    for i in range(0,len(triangulation)):
	    triangulation[i].draw(canvas,"blue")

    for i in range(0,len(points)):
        print inTriangle(triangulation[0],points[i])

    canvas.pack()
    window.mainloop()


