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
        #print "flipping point" + str(point) + " en triangulo " + str(triangle) + " y arista " + str(edge) + "punto vecino es" + str(neighbour.getThirdPoint(edge))

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

    #print "triangulo 1 antes" + str(triangle1)
    #print "triangulo 2 antes" + str(triangle2)

    #Guardar los vecinos originales, antes de cambiar los vertices de los triangulos
    n1T1 = triangle1.getNeighbourFromEdge(Edge(edge.p2,pointP))
    n2T1 = triangle1.getNeighbourFromEdge(Edge(pointP,edge.p1))

    n1T2 = triangle2.getNeighbourFromEdge(Edge(edge.p1,pointQ))
    n2T2 = triangle2.getNeighbourFromEdge(Edge(pointQ,edge.p2))

    triangle1.setPoints(pointP,edge.p1,pointQ)
    triangle2.setPoints(pointP,pointQ,edge.p2)

    #print "triangulo 1 despues" + str(triangle1)
    #print "triangulo 2 despues" + str(triangle2)
    #print ""

    triangle1.setNeighbours(n2T1,n1T2,triangle2)
    triangle2.setNeighbours(n2T2,n1T1,triangle1)

    #Notificar a los vecinos que ha cambiado quien esta junto a el. Importante no notificar a vecinos None
    if n1T1 is not None:
        n1T1.setNeighbourByEdge(Edge(edge.p2,pointP),triangle2)

    if n2T1 is not None:
        n2T1.setNeighbourByEdge(Edge(pointP,edge.p1),triangle1)

    if n1T2 is not None:
        n1T2.setNeighbourByEdge(Edge(edge.p1,pointQ),triangle1)

    if n2T2 is not None:
        n2T2.setNeighbourByEdge(Edge(pointQ,edge.p2),triangle2)

    return Edge(pointP,pointQ)
