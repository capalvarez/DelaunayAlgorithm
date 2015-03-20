__author__ = 'cata'

from CircleTest import circleTest
import Triangle
import Edge

def legalizeEdge(point,edge,triangle,triangulation):
    #Revisa localmente si el triangulo generado es o no Delaunay; si no lo es, hace flip y se propaga a los vecinos
    neighbour = triangle.getNeighbourFromEdge(edge)

    if circleTest(point,edge.p1,edge.p2,neighbour.getThirdPoint(edge)):
        #Hacer intercambio de diagonales
        newTriangles = flipEdge(triangle,neighbour,edge)

        #Buscar en la triangulacion los triangulos iniciales, y eliminarlos
        triangulation.remove(triangle)
        triangulation.remove(neighbour)

        #Incluir los nuevos triangulos enla triangulacion
        triangulation = triangulation + newTriangles

        #Se deben legalizar los dos nuevos triangulos, por lo que se requiere informacion de ellos
        legalizeEdge(point,newTriangles[0].getEdgeWithoutPoint(point),newTriangles[0],triangulation)
        legalizeEdge(point,newTriangles[1].getEdgeWithoutPoint(point),newTriangles[1],triangulation)

def flipEdge(triangle1,triangle2,edge):
    pointP = triangle1.getThirdPoint(edge)
    pointQ = triangle2.getThirdPoint(edge)

    newTriangle1 = Triangle(pointP,edge.p1,pointQ)
    newTriangle2 = Triangle(pointP,pointQ,edge.p2)

    newTriangle1.setNeighbours(triangle1.getNeighbourFromEdge(Edge(pointP,edge.p1)),triangle2.getNeighbourFromEdge(Edge(edge.p1,pointQ)),newTriangle2)
    newTriangle2.setNeighbours(triangle2.getNeighbourFromEdge(Edge(pointQ,edge.p2)),triangle1.getNeighbourFromEdge(Edge(edge.p2,pointP)),newTriangle2)

    return [newTriangle1,newTriangle2]


