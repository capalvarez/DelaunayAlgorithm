__author__ = 'cata'

from Edge import Edge
from random import randint

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


def findTriangleLineal(triangles,point):
    #Recibe un punto y una lista de triangulos, devuelve el triangulo en el que se encuentra el punto
    for i in range(0,len(triangles)):
        if inTriangle(triangles[i],point):
            return triangles[i]

def findTriangleJumpWalk(triangles,point):
    #Recibe un punto y una lista de triangulos, devuelve el triangulo en el que se encuentra el punto

    #Walk and jump para encontrar los triangulos en mejor tiempo promedio
    #Elige un triangulo al azar en el que comenzar la busqueda
    t = chooseTriangle(triangles)

    #Antes de empezar la busqueda, verificamos no haber tenido la suerte de encontrar de inmediato el triangulo buscado
    if inTriangle(t,point):
        return t

    #Obtener los puntos relevantes del triangulo, tomamos el primer vertice como el inicio de la busqueda
    q = t.p1
    left = t.p2
    right = t.p3

    #Etapa de inicializacion, buscamos un triangulo por el cual pase el segmento que une q y point
    if orientTest(right,q,point)<0:
        while orientTest(left,q,point)<0:
            right = left
            t = t.getNeighbourFromEdge(Edge(q,left))

            #No podemos avanzar hacia afuera del triangulo contenedor
            if t is None:
                continue

            left = t.getThirdPoint(Edge(q,right))
    else:
        while True:
            left = right
            t = t.getNeighbourFromEdge(Edge(q,right))

            #No podemos avanzar hacia afuera del triangulo contenedor
            if t is None:
                continue

            right = t.getThirdPoint(Edge(q,left))

            if orientTest(right,q,point)<0:
                break

    #Comenzamos la caminata
    while orientTest(point,right,left)<0:
        t = t.getNeighbourFromEdge(Edge(right,left))

        if t is None:
            continue

        s = t.getThirdPoint(Edge(right,left))

        if orientTest(s,q,point)<0:
            right = s
        else:
            left = s

    return t

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

def chooseTriangle(triangles):
    index = randint(0,len(triangles)-1)

    return triangles[index]

