__author__ = 'cata'

from Utilities import *
from Point import Point2D
from Triangle import Triangle
from Tkinter import *

def inTriangle(triangle,point):
    #Recibe un triangulo y un punto y decide si el punto esta dentro del triangulo, usando el test de la orientacion
    edges = triangle.getEdges()

    #Verificar aristas en orden, de tal forma que si una falla no continuar
    if orientTest(edges[0].p1,point,edges[0].p2) < 0:
        return False

    if orientTest(edges[1].p1,point,edges[1].p2) < 0:
        return False

    if orientTest(edges[2].p1,point,edges[2].p2) < 0:
        return False

    return True

def orientTest(pA,pB,pC):
    return (pB.getX() - pA.getX())*(pC.getY() - pA.getY()) - (pC.getX() - pA.getX())*(pB.getY() - pA.getY())

def findTriangle(triangles,point):
    #Recibe un punto y una lista de triangulos, devuelve el triangulo en el que se encuentra el punto

    for i in range(0,len(triangles)):
        if inTriangle(triangles[i],point):
            return triangles[i]

    window = Tk()
    frame = Frame(window)
    frame.pack()

    canvas = Canvas(window,width=600,height=400,bg="white")

    print "estoy retornando none"
    print point
    for i in range(0,len(triangles)):
        print triangles[i]

    point.draw(canvas)

    for i in range(0,len(triangles)):
	    triangles[i].draw(canvas,"blue")

    canvas.pack()
    window.mainloop()

def insideTriangle(triangle,point):
    edges = triangle.getEdges()

    #Verificar aristas en orden, de tal forma que si una falla no continuar
    if orientTest(edges[0].p1,point,edges[0].p2) == 0:
        return [False,edges[0]]

    if orientTest(edges[1].p1,point,edges[1].p2) == 0:
        return [False,edges[1]]

    if orientTest(edges[2].p1,point,edges[2].p2) == 0:
        return [False,edges[2]]

    return [True,None]


if __name__ == '__main__':
    #points = randomPoints(1,50,300)
    points = [Point2D(120,120)]

    window = Tk()
    frame = Frame(window)
    frame.pack()

    canvas = Canvas(window,width=600,height=400,bg="white")
    #triangulation = randomTriangles(1,50,300)
    triangulation = [Triangle(Point2D(100,100),Point2D(100,200),Point2D(200,100))]

    for i in range(0,len(points)):
    	points[i].draw(canvas)


    for i in range(0,len(triangulation)):
	    triangulation[i].draw(canvas,"blue")

    print inTriangle(triangulation[0],points[0])

    canvas.pack()
    window.mainloop()




