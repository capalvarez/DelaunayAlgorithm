__author__ = 'cata'

from CircleTest import circleTest
from Triangle import Triangle
from Edge import Edge

def legalizeEdge(point,edge,triangle):
    #Revisa localmente si el triangulo generado es o no Delaunay; si no lo es, hace flip y se propaga a los vecinos
    neighbour = triangle.getNeighbourFromEdge(edge)   
    	
    if neighbour is None:
         return

    if  circleTest(point,edge.p1,edge.p2,neighbour.getThirdPoint(edge)) >= 0:
        #Hacer intercambio de diagonales
        newEdge = flipEdge(triangle,neighbour,edge)
      
        #Se deben legalizar los dos nuevos triangulos
        legalizeEdge(point,triangle.getEdgeWithoutPoint(point),triangle)
        legalizeEdge(point,neighbour.getEdgeWithoutPoint(point),neighbour)

def flipEdge(triangle1,triangle2,edge):
    pointP = triangle1.getThirdPoint(edge)
    pointQ = triangle2.getThirdPoint(edge)

    triangle1.setPoints(pointP,edge.p1,pointQ)
    triangle2.setPoints(pointP,pointQ,edge.p2)

    triangle1.setNeighbours(triangle1.getNeighbourFromEdge(Edge(pointP,edge.p1)),triangle2.getNeighbourFromEdge(Edge(edge.p1,pointQ)),triangle2)
    triangle2.setNeighbours(triangle2.getNeighbourFromEdge(Edge(pointQ,edge.p2)),triangle1.getNeighbourFromEdge(Edge(edge.p2,pointP)),triangle1)

    return Edge(pointP,pointQ)
