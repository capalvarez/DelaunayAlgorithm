__author__ = 'cata'

from Edge import Edge
from Point import *
from Tkinter import *

class Triangle:
    def __init__(self,p1,p2,p3):
        #Recibe tres puntos (basicamente trabaja por referencia)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.n1 = None
        self.n2 = None
        self.n3 = None

    def draw(self,canvas,color):
        Edge(self.p1,self.p2).draw(canvas,color)
        Edge(self.p2,self.p3).draw(canvas,color)
        Edge(self.p3,self.p1).draw(canvas,color)

    def getEdges(self):
        return [Edge(self.p1,self.p2),Edge(self.p2,self.p3),Edge(self.p3,self.p1)]

    def getPoints(self):
        return [self.p1,self.p2,self.p3]

    def setNeighbours(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def getNeighbours(self):
        return [self.n1,self.n2,self.n3]

    def setPoints(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def findThirdPoint(self,edge):
        points = self.getPoints()
        points.remove(edge.p1)
        points.remove(edge.p2)

        return points[0]

    def getNeighbourFromEdge(self,edge):
        neighbours = [self.n1,self.n2,self.n3]

        for i in range(0,len(neighbours)):
            if neighbours[i]!=None and neighbours[i].isEdge(edge):
                return neighbours[i]

    def isEdge(self,edge):
        points = self.getPoints()

        if edge.p1 in points:
            if edge.p2 in points:
                return True

        return False

    def getEdgeWithoutPoint(self,point):
        if point == self.p1:
            return Edge(self.p2,self.p3)
        elif point == self.p2:
            return Edge(self.p3,self.p1)
        else:
            return Edge(self.p1,self.p2)

    def getThirdPoint(self,edge):
        points = self.getPoints()
        points.remove(edge.p1)
        points.remove(edge.p2)

        return points[0]

    def setNeighbourByIndex(self,index,newNeighbour):
        if index==0:
            self.n1 = newNeighbour
        elif index==1:
            self.n2 = newNeighbour
        elif index==2:
            self.n3 = newNeighbour

    def getDifferentEdges(self,newEdge):
	edges = self.getEdges()
        
        for i in range(0,len(edges)):
		if edges[i].equals(newEdge):
			edges.remove(edges[i])
			return edges

    def findNeighbour(self,possibleNeighbours):
        for i in range(0,len(possibleNeighbours)):
            if self.commonEdge(possibleNeighbours[i]) is not None:
                return [self.commonEdge(possibleNeighbours[i]),possibleNeighbours[i]]

        print "sali sin nada =("

    def commonEdge(self,triangle):
        points1 = self.getPoints()
        points2 = triangle.getPoints()

        commonPoints = list(set(points1) & set(points2))

        #Hay exactamente dos puntos en comun entre los triangulos->tienen arista en comun
        if len(commonPoints) == 2:
            return Edge(commonPoints[0],commonPoints[1])
        else:
            return None

    def notifyNeighbours(self,newNeighbours):
        print self
        print map(lambda x: str(x),self.getNeighbours())
        print map(lambda x: str(x),newNeighbours)
        if self.n1 is not None:
            [commonEdge1,newNeighbour1] = self.n1.findNeighbour(newNeighbours)
            print "arista comun1" + str(commonEdge1)
            print "vecino encontrado1" + str(newNeighbour1)
            self.n1.setNeighbourByEdge(commonEdge1,newNeighbour1)

        if self.n2 is not None:
            print "vecino 2" + str(self.n2)
            [commonEdge2,newNeighbour2] = self.n2.findNeighbour(newNeighbours)
            print "arista comun2" + str(commonEdge2)
            print "vecino encontrado2" + str(newNeighbour2)
            self.n2.setNeighbourByEdge(commonEdge2,newNeighbour2)

        if self.n3 is not None:
            [commonEdge3,newNeighbour3] = self.n3.findNeighbour(newNeighbours)
            print "arista comun3" + str(commonEdge3)
            print "vecino encontrado3" + str(newNeighbour3)
            self.n3.setNeighbourByEdge(commonEdge3,newNeighbour3)

    def setNeighbourByEdge(self,edge,newNeighbour):
        neighbours = self.getNeighbours()

        #print "triangulo " + str(self) + "arista " + str(edge) + "vecino a asignar " + str(newNeighbour)

        for i in range(0,len(neighbours)):
            if neighbours[i] is not None and neighbours[i].isEdge(edge):
                #print "vecino encontrado " + str(neighbours[i])
                #print neighbours[i]
                self.setNeighbourByIndex(i,newNeighbour)

    def __str__(self):
        return str(self.p1) + str(self.p2) + str(self.p3)

    def printNeighbours(self):
        print "vecinos: " + str(self.n1) + "  " + str(self.n2) + "   " + str(self.n3)







