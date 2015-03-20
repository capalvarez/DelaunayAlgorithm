__author__ = 'cata'

from BigTriangle import bigTriangle
from FindTriangle import findTriangle
from random import shuffle
from Legalize import legalizeEdge
import Triangle


def delaunay(points):
    #Encontrar el triangulo inicial de la triangulacion
    baseTriangle = bigTriangle(points)

    #Incluir el triangulo ficticio en la triangulacion, se debe eliminar posteriormente
    triangulation = [baseTriangle]

    #Hacer una permutacion aleatoria de los puntos (mejora rendimiento)
    points = shuffle(points)

    #Ir agregando los puntos a la triangulacion uno o uno
    for i in range(0,len(points)):
        #Tomar un nuevo punto y encontrar el triangulo que lo contiene (ojo, por ahora me bypasseo el problema de que
        # este en una arista)
        conT = findTriangle(triangulation,points[i])

        if esta dentro del triangulo
            #Se crean tres nuevos triangulos
            newTriangle1 = Triangle(points[i],conT.p1,conT.p2)
            newTriangle2 = Triangle(points[i],conT.p2,conT.p3)
            newTriangle3 = Triangle(points[i],conT.p3,conT.p1)

            #Se asignan los vecinos correspondientes a cada triangulo, notar que van en orden antihorario
            newTriangle1.setNeighbours(conT.n1,newTriangle2,newTriangle3)
            newTriangle2.setNeighbours(newTriangle1,conT.n2,newTriangle3)
            newTriangle3.setNeighbours(newTriangle1,newTriangle2,conT.n3)

            newTriangles = [newTriangle1,newTriangle2,newTriangle3]

            #Hay que eliminar el triangulo antiguo
            triangulation.remove(conT)

            #Incluir los nuevos triangulos en la triangulacion
            triangulation = triangulation + newTriangles

            #Legalizar los nuevos triangulos
            legalizeEdge(points[i],newTriangle1.getEdgeWithoutPoint(points[i]),newTriangle1,triangulation)
            legalizeEdge(points[i],newTriangle2.getEdgeWithoutPoint(points[i]),newTriangle2,triangulation)
            legalizeEdge(points[i],newTriangle3.getEdgeWithoutPoint(points[i]),newTriangle3,triangulation)





