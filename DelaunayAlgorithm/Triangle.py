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

        for i in (0,2):
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
        else:
            self.n3 = newNeighbour

    def getDifferentEdges(self,newEdge):
	edges = self.getEdges()
        
        for i in range(0,len(edges)):
		if edges[i].equals(newEdge):
			edges.remove(edges[i])
			return edges

    def notifyNeighbours(self,newNeighbours):
        if self.n1 is not None:
            self.n1.setNeighbourByEdge(Edge(self.p1,self.p2),newNeighbours[0])

        if self.n2 is not None:
            self.n2.setNeighbourByEdge(Edge(self.p2,self.p3),newNeighbours[1])

        if self.n3 is not None:
            self.n3.setNeighbourByEdge(Edge(self.p3,self.p1),newNeighbours[2])

    def setNeighbourByEdge(self,edge,newNeighbour):
        neighbours = self.getNeighbours()

        for i in range(0,len(neighbours)):
            if neighbours[i] is not None:
                if neighbours[i].isEdge(edge):
                    self.setNeighbourByIndex(i,newNeighbour)

    def __str__(self):
        return str(self.p1) + str(self.p2) + str(self.p3)

    def printNeighbours(self):
        print "vecinos: " + str(self.n1) + "  " + str(self.n2) + "   " + str(self.n3)







