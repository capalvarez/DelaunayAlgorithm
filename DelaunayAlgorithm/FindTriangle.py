__author__ = 'cata'

from Utilities import *

def inTriangle(triangle,point):
    #Recibe un triangulo y un punto y decide si el punto esta dentro del triangulo, usando el test de la orientacion
    edges = triangle.getEdges()

    #Verificar aristas en orden, de tal forma que si una falla no continuar
    if orientTest((edges[0].p1,edges[0].p2,point)) < 0:
        return False

    if orientTest((edges[1].p1,edges[1].p2,point)) < 0:
        return False

    if orientTest((edges[2].p1,edges[2].p2,point)) < 0:
        return False

    return True

def orientTest(points):
    return sign ((points[0].getX()-points[2].getX())*(points[1].getY()-points[2].getY()) - \
                 (points[1].getX()-points[2].getX())*(points[0].getY()-points[2].getY()))

def findTriangle(triangles,point):
    #Recibe un punto y una lista de triangulos, devuelve el triangulo en el que se encuentra el punto (definir que pasa
    # si esta en una arista PENDIENTE)
    i = 0

    while i < len(triangles):
        if inTriangle(triangles[i],point):
            return triangles[i]

    #Por ahora no veo este caso
    return 0


