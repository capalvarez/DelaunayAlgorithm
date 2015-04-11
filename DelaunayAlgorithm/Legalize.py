__author__ = 'cata'

from CircleTest import circleTest,CClockwise
from Triangle import Triangle
from Edge import Edge
from Utilities import findAndRemove


def legalizeEdge(point,edge,triangle,triangulation):
    #Revisa localmente si el triangulo generado es o no Delaunay; si no lo es, hace flip y se propaga a los vecinos
    print "entrando a un legalizeEdge"
    print "contenido actual de la triangulacion"
    for k in range(0,len(triangulation)):
        print triangulation[k]

    neighbour = triangle.getNeighbourFromEdge(edge)

    if neighbour is None:
         return

    if  circleTest(point,edge.p1,edge.p2,neighbour.getThirdPoint(edge)) < 0:
        print "flipping point" + str(point) + " en triangulo " + str(triangle) + " y arista " + str(edge) + "punto vecino es" + str(neighbour.getThirdPoint(edge))
        print neighbour in triangulation

        #Hacer intercambio de diagonales
        print "triangulo antes" + str(triangle)
        print "vecino antes" + str(neighbour)

        newEdge = flipEdge(triangle,neighbour,edge,triangulation)

        print "triangulo despues" + str(triangle)
        print "vecino despues" + str(neighbour)

        #Se deben legalizar los dos nuevos triangulos
        edgesT = triangle.getDifferentEdges(newEdge)
        edgesN = neighbour.getDifferentEdges(newEdge)

        legalizeEdge(point,edgesT[0],triangle,triangulation)
        legalizeEdge(point,edgesT[1],triangle,triangulation)
        legalizeEdge(point,edgesN[0],neighbour,triangulation)
        legalizeEdge(point,edgesN[1],neighbour,triangulation)

        print neighbour in triangulation

    #else:
        #print "not flipping point" + str(point) + " en triangulo " + str(triangle) + " y arista " + str(edge) + "punto vecino es" + str(neighbour.getThirdPoint(edge))

def flipEdge(triangle1,triangle2,edge,triangulation):
    pointP = triangle1.getThirdPoint(edge)
    pointQ = triangle2.getThirdPoint(edge)

    #print "triangulo 1 antes" + str(triangle1)
    #print "triangulo 2 antes" + str(triangle2)
    #print ""

    #Guardar los vecinos originales, antes de cambiar los vertices de los triangulos
    n1T1 = triangle1.getNeighbourFromEdge(Edge(edge.p2,pointP))
    if n1T1 is not None:
        #print "vecinos de n1T1 antes de copy"
        #print map(lambda x: str(x),n1T1.getNeighbours())
        n1T1Neighbours = n1T1.copyNeighbours()

    n2T1 = triangle1.getNeighbourFromEdge(Edge(pointP,edge.p1))
    if n2T1 is not None:
        n2T1Neighbours = n2T1.copyNeighbours()

    n1T2 = triangle2.getNeighbourFromEdge(Edge(edge.p1,pointQ))
    if n1T2 is not None:
        n1T2Neighbours = n1T2.copyNeighbours()

    n2T2 = triangle2.getNeighbourFromEdge(Edge(pointQ,edge.p2))
    if n2T2 is not None:
        n2T2Neighbours = n2T2.copyNeighbours()

    triangle1.setPoints(pointP,edge.p1,pointQ)
    triangle2.setPoints(pointP,pointQ,edge.p2)

    triangle1.setNeighbours(n2T1,n1T2,triangle2)
    triangle2.setNeighbours(n2T2,n1T1,triangle1)

    #print "triangulo 1 despues" + str(triangle1)
    #print "triangulo 2 despues" + str(triangle2)
    #print ""

    #Notificar a los vecinos que ha cambiado quien esta junto a el.
    if n1T1 is not None:
        old = n1T1.getNeighbours()
        n1T1.setNeighbours(n1T1Neighbours[0],n1T1Neighbours[1],n1T1Neighbours[2])

        for i in range(0,len(old)):
            findAndRemove(triangulation,old[i])

        #print "n1T1" + str(n1T1)
        #print str(Edge(edge.p2,pointP))
        #print "vecinos antes"
        #print map(lambda x: str(x),n1T1.getNeighbours())
        n1T1.setNeighbourByEdge(Edge(edge.p2,pointP),triangle2)
        triangulation = triangulation + n1T1Neighbours
        #print "vecinos despues"
        #print map(lambda x: str(x),n1T1.getNeighbours())

    if n2T1 is not None:
        old = n2T1.getNeighbours()
        n2T1.setNeighbours(n2T1Neighbours[0],n2T1Neighbours[1],n2T1Neighbours[2])

        for i in range(0,len(old)):
            findAndRemove(triangulation,old[i])

        #print "n2T1" + str(n2T1)
        #print "vecinos antes"
        #print map(lambda x: str(x),n2T1.getNeighbours())
        n2T1.setNeighbourByEdge(Edge(pointP,edge.p1),triangle1)
        triangulation = triangulation + n2T1Neighbours
        #print "vecinos despues"
        #print map(lambda x: str(x),n2T1.getNeighbours())

    if n1T2 is not None:
        old = n1T2.getNeighbours()
        n1T2.setNeighbours(n1T2Neighbours[0],n1T2Neighbours[1],n1T2Neighbours[2])
        print "vecino 1" + str(old[0]) + str(old[0] in triangulation)
        print "vecino 2" + str(old[1]) + str(old[1] in triangulation)
        print "vecino 3" + str(old[2]) + str(old[2] in triangulation)

        print "n1T2" + str(n1T2)
        print "vecinos antes"
        print map(lambda x: str(x),n1T2.getNeighbours())
        for i in range(0,len(old)):
            findAndRemove(triangulation,old[i])

        n1T2.setNeighbourByEdge(Edge(edge.p1,pointQ),triangle1)
        triangulation = triangulation + n1T2Neighbours

        print "vecinos despues"
        print map(lambda x: str(x),n1T2.getNeighbours())
        print "contenido actual de la triangulacion"
        for k in range(0,len(triangulation)):
            print triangulation[k]


    if n2T2 is not None:
        old = n2T2.getNeighbours()
        n2T2.setNeighbours(n2T2Neighbours[0],n2T2Neighbours[1],n2T2Neighbours[2])

        for i in range(0,len(old)):
            findAndRemove(triangulation,old[i])

        #print "n2T2" + str(n2T2)
        #print "vecinos antes"
        #print map(lambda x: str(x),n2T2.getNeighbours())
        n2T2.setNeighbourByEdge(Edge(pointQ,edge.p2),triangle2)
        triangulation = triangulation + n2T2Neighbours
        #print "vecinos despues"
        #print map(lambda x: str(x),n2T2.getNeighbours())

    return Edge(pointP,pointQ)
