__author__ = 'cata'

from BigTriangle import bigTriangle
from FindTriangle import findTriangle
from random import shuffle
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

        #if esta dentro del triangulo
        #Se crean tres nuevos triangulos
        newTriangles = [Triangle(points[i],conT.p1,conT.p2),Triangle(points[i],conT.p2,conT.p3),Triangle(points[i],conT.p3,conT.p1)]

        #Hay que eliminar el triangulo antiguo
        triangulation.remove(conT)

        #Legalizar los nuevos triangulos




