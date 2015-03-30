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
    n2T1 = triangle1.getNeighbourFromEdge(Edge(pointP,edge.p1))

    n1T2 = triangle2.getNeighbourFromEdge(Edge(edge.p1,pointQ))
    n2T2 = triangle2.getNeighbourFromEdge(Edge(pointQ,edge.p2))

    triangle1.setPoints(pointP,edge.p1,pointQ)
    triangle2.setPoints(pointP,pointQ,edge.p2)

    triangle1.setNeighbours(n2T1,n1T2,triangle2)
    triangle2.setNeighbours(n2T2,n1T1,triangle1)

    return Edge(pointP,pointQ)
