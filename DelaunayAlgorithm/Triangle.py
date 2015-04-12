__author__ = 'cata'

from Edge import Edge

class Triangle:
    def __init__(self,p1,p2,p3):
        #Recibe tres puntos (basicamente trabaja por referencia)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.n1 = None
        self.n2 = None
        self.n3 = None

    def equals(self,other):
        return self.p1==other.p1 and self.p2==other.p2 and self.p3==other.p3

    def getTriangle(self):
        return Triangle(self.p1.getPoint(),self.p2.getPoint(),self.p3.getPoint())

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

    def setNeighboursPoints(self,n1,n2,n3):
        if self.n1 is not None:
            print "vecino a asignar" + str(n1)
            self.n1.setPointsByTriangle(n1)
            print "lo que quedo" + str(self.n1)

        if self.n2 is not None:
            self.n2.setPointsByTriangle(n2)
            print "lo que quedo despues de n2" + str(self.n1)

        if self.n3 is not None:
            self.n3.setPointsByTriangle(n3)
            print "lo que quedo despues de n3" + str(self.n1)

        print "resultados de la asignacion"
        print map(lambda x: str(x),self.getNeighbours())


    def setPointsByTriangle(self,otherT):
        self.p1 = otherT.p1
        self.p2 = otherT.p2
        self.p3 = otherT.p3

    def getNeighbours(self):
        return [self.n1,self.n2,self.n3]

    def copyNeighbours(self):
        if self.n1 is not None:
            t1 = self.n1.getTriangle()
        else:
            t1 = None

        if self.n2 is not None:
            t2 = self.n2.getTriangle()
        else:
            t2 = None

        if self.n3 is not None:
            t3 = self.n3.getTriangle()
        else:
            t3 = None

        return [t1,t2,t3]

    def setPoints(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def getNeighbourFromEdge(self,edge):
        neighbours = [self.n1,self.n2,self.n3]
        #print map(lambda x: str(x),neighbours)

        for i in range(0,len(neighbours)):
            if neighbours[i]!=None and neighbours[i].isEdge(edge):
                return neighbours[i]

    def isEdge(self,edge):
        #print "soy " + str(self) + "y la arista es "+ str(edge)
        points = self.getPoints()

        for i in range(0,len(points)):
            if edge.p1.equals(points[i]):
                for j in range(0,len(points)):
                    if edge.p2.equals(points[j]):
                        #print "es arista!"
                        return True

        return False

    def getEdgeWithoutPoint(self,point):
        if point.equals(self.p1):
            return Edge(self.p2,self.p3)
        elif point.equals(self.p2):
            return Edge(self.p3,self.p1)
        else:
            return Edge(self.p1,self.p2)

    def getThirdPoint(self,edge):
        points = self.getPoints()

        for i in range(0,len(points)):
            if edge.p1.equals(points[i]):
                points.remove(points[i])
                break

        for i in range(0,len(points)):
            if edge.p2.equals(points[i]):
                points.remove(points[i])
                break

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
        print "findNeighbour, quien soy" + str(self)
        print "posibles vecinos"
        print map(lambda x: str(x),possibleNeighbours)

        for i in range(0,len(possibleNeighbours)):
            if self.commonEdge(possibleNeighbours[i]) is not None:
                return [self.commonEdge(possibleNeighbours[i]),possibleNeighbours[i]]

        print "sali sin nada =("

    def commonEdge(self,triangle):
        points1 = self.getPoints()
        points2 = triangle.getPoints()
        commonPoints = []

        for i in range(0,len(points1)):
            for j in range(0,len(points2)):
                if points1[i].equals(points2[j]):
                    commonPoints = commonPoints + [points1[i]]

        #Hay exactamente dos puntos en comun entre los triangulos->tienen arista en comun
        if len(commonPoints) == 2:
            return Edge(commonPoints[0],commonPoints[1])
        else:
            return None

    def notifyNeighbours(self,newNeighbours):
        #print self
        #print map(lambda x: str(x),self.getNeighbours())
        #print map(lambda x: str(x),newNeighbours)
        if self.n1 is not None:
            print "n1" + str(self.n1)
            print "vecinos de n1"
            print map(lambda x: str(x),self.n1.getNeighbours())
            [commonEdge1,newNeighbour1] = self.n1.findNeighbour(newNeighbours)
            #print "arista comun1" + str(commonEdge1)
            #print "vecino encontrado1" + str(newNeighbour1)
            self.n1.setNeighbourByEdge(commonEdge1,newNeighbour1)

        if self.n2 is not None:
            print "n2" + str(self.n2)
            print "vecinos de n2"
            print map(lambda x: str(x),self.n2.getNeighbours())
            #print "vecino 2" + str(self.n2)
            [commonEdge2,newNeighbour2] = self.n2.findNeighbour(newNeighbours)
            #print "arista comun2" + str(commonEdge2)
            #print "vecino encontrado2" + str(newNeighbour2)
            self.n2.setNeighbourByEdge(commonEdge2,newNeighbour2)

        if self.n3 is not None:
            print "n3" + str(self.n3)
            print "vecinos de n3"
            print map(lambda x: str(x),self.n3.getNeighbours())
            #print "vecino 3" + str(self.n3)
            [commonEdge3,newNeighbour3] = self.n3.findNeighbour(newNeighbours)
            #print "arista comun3" + str(commonEdge3)
            #print "vecino encontrado3" + str(newNeighbour3)
            self.n3.setNeighbourByEdge(commonEdge3,newNeighbour3)

    def setNeighbourByEdge(self,edge,newNeighbour):
        neighbours = self.getNeighbours()

        #print "triangulo " + str(self) + " arista " + str(edge) + " vecino a asignar " + str(newNeighbour)

        for i in range(0,len(neighbours)):
            if neighbours[i] is not None and neighbours[i].isEdge(edge):
                #print "vecino encontrado " + str(neighbours[i])
                #print neighbours[i]
                self.setNeighbourByIndex(i,newNeighbour)

    def __str__(self):
        return str(self.p1) + str(self.p2) + str(self.p3)

    def printNeighbours(self):
        print "vecinos: " + str(self.n1) + "  " + str(self.n2) + "   " + str(self.n3)







