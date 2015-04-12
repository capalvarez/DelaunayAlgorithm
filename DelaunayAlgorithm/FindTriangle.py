__author__ = 'cata'

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



