__author__ = 'cata'

from CircleTest import circleTest,CClockwise
from Triangle import Triangle
from Edge import Edge

def legalizeEdge(point,edge,triangle):
    #Revisa localmente si el triangulo generado es o no Delaunay; si no lo es, hace flip y se propaga a los vecinos
    neighbour = triangle.getNeighbourFromEdge(edge)   
    #print "vecino" + str(neighbour)

    if neighbour is None:
         return

    if  circleTest(point,edge.p1,edge.p2,neighbour.getThirdPoint(edge)) < 0:
        print "flipping point" + str(point) + " en triangulo " + str(triangle) + " y arista " + str(edge) + "punto vecino es" + str(neighbour.getThirdPoint(edge))

        #Hacer intercambio de diagonales
        newEdge = flipEdge(triangle,neighbour,edge)

        #Se deben legalizar los dos nuevos triangulos
        edgesT = triangle.getDifferentEdges(newEdge)
        edgesN = neighbour.getDifferentEdges(newEdge)

        legalizeEdge(point,edgesT[0],triangle)
        legalizeEdge(point,edgesT[1],triangle)
        legalizeEdge(point,edgesN[0],neighbour)
        legalizeEdge(point,edgesN[1],neighbour)
    #else:
        #print "not flipping point" + str(point) + " en triangulo " + str(triangle) + " y arista " + str(edge) + "punto vecino es" + str(neighbour.getThirdPoint(edge))

def flipEdge(triangle1,triangle2,edge):
    pointP = triangle1.getThirdPoint(edge)
    pointQ = triangle2.getThirdPoint(edge)

    #Guardar los vecinos originales, antes de cambiar los vertices de los triangulos
    n1T1 = triangle1.getNeighbourFromEdge(Edge(edge.p2,pointP))
    if n1T1 is not None:
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
        n1T1.setNeighbours(n1T1Neighbours[0],n1T1Neighbours[1],n1T1Neighbours[2])
        #print "n1T1" + str(n1T1)
        #print str(Edge(edge.p2,pointP))
        #print "vecinos antes"
        #print map(lambda x: str(x),n1T1.getNeighbours())
        n1T1.setNeighbourByEdge(Edge(edge.p2,pointP),triangle2)
        #print "vecinos despues"
        #print map(lambda x: str(x),n1T1.getNeighbours())

    if n2T1 is not None:
        n2T1.setNeighbours(n2T1Neighbours[0],n2T1Neighbours[1],n2T1Neighbours[2])
        #print "n2T1" + str(n2T1)
        #print "vecinos antes"
        #print map(lambda x: str(x),n2T1.getNeighbours())
        n2T1.setNeighbourByEdge(Edge(pointP,edge.p1),triangle1)
        #print "vecinos despues"
        #print map(lambda x: str(x),n2T1.getNeighbours())

    if n1T2 is not None:
        n1T2.setNeighbours(n1T2Neighbours[0],n1T2Neighbours[1],n1T2Neighbours[2])
        #print "n1T2" + str(n1T2)
        #print "vecinos antes"
        #print map(lambda x: str(x),n1T2.getNeighbours())
        n1T2.setNeighbourByEdge(Edge(edge.p1,pointQ),triangle1)
        #print "vecinos despues"
        #print map(lambda x: str(x),n1T2.getNeighbours())

    if n2T2 is not None:
        n2T2.setNeighbours(n2T2Neighbours[0],n2T2Neighbours[1],n2T2Neighbours[2])
        n2T2.setNeighbourByEdge(Edge(pointQ,edge.p2),triangle2)

    return Edge(pointP,pointQ)
