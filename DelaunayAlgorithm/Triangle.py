__author__ = 'cata'

from Edge import *
from Point import *

class Triangle:
    def __init__(self,p1,p2,p3):
        #Recibe tres puntos (basicamente trabaja por referencia)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.n1 = None
        self.n2 = None
        self.n3 = None

    def getPoints(self):
        return [self.p1,self.p2,self.p3]

    def commonEdge(self, triangle):
        #Recibe un segundo triangulo y devuelve la arista comun entre ambos
        points1 = self.getPoints()
        points2 = triangle.getPoints()

        return set(points1).intersection(points2)

    def setNeighbours(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def findThirdPoint(self,edge):
        points = self.getPoints()
        points.remove(edge.p1)
        points.remove(edge.p2)

        return points[0]

    def getNeighbourFromEdge(self,edge):
        neighbours = [self.n1,self.n2,self.n3]

        for i in (0,2):
            if neighbours[i].isEdge(edge):
                return neighbours[i]

    def isEdge(self,edge):
        points = self.getPoints()
        points.remove(edge.p1)
        points.remove(edge.p2)

        return len(points) > 0

    def getEdgeWithoutPoint(self,point):
        if point == self.p1:
            return Edge(self.p2,self.p3)
        elif point == self.p2:
            return Edge(self.p3,self.p1)
        else:
            return Edge(self.p1,self.p2)

if __name__ == '__main__':
    point1 = Point2D(0,0)
    point2 = Point2D(1,0)
    point3 = Point2D(1,1)

    edge = Edge(point1,point2)
    triangle = Triangle(point1,point2,point3)

    print triangle.findThirdPoint(edge)





