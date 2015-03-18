__author__ = 'cata'

from Edge import *
from Point import *

class Triangle:
    def __init__(self,p1,p2,p3):
        #Recibe tres puntos (basicamente trabaja por referencia)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def getEdges(self):
        return (Edge(self.p1,self.p2),Edge(self.p2,self.p3),Edge(self.p3,self.p1))

    def getPoints(self):
        return (self.p1,self.p2,self.p3)

    def commonEdge(self, triangle):
        #Recibe un segundo triangulo y devuelve la arista comun entre ambos
        points1 = self.getPoints()
        points2 = triangle.getPoints()

        return set(points1).intersection(points2)

