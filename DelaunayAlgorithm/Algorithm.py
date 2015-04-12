__author__ = 'cata'

from BigTriangle import bigTriangle
from FindTriangle import findTriangle, insideTriangle
from Legalize import legalizeEdge
from Point import Point2D
from Edge import Edge
from Triangle import Triangle 
from Tkinter import *
from RandomGenerator import randomPoints

def delaunay(points,canvas):
    #Encontrar el triangulo inicial de la triangulacion
    baseTriangle = bigTriangle(points,0.3)

    #Incluir el triangulo ficticio en la triangulacion, se debe eliminar posteriormente
    triangulation = [baseTriangle]

    #Ir agregando los puntos a la triangulacion uno o uno
    for i in range(0,len(points)):
        #Tomar un nuevo punto y encontrar el triangulo que lo contiene
        conT = findTriangle(triangulation,points[i])
        [inside,conEdge] = insideTriangle(conT,points[i])
	
        if inside:
            print "Punto agregando " + str(points[i])
            print "Triangulo contenedor" + str(conT)
            #print "contenido actual de la triangulacion"
            #for k in range(0,len(triangulation)):
            #    print triangulation[k]

            neighbours = conT.getNeighbours()
            print "vecinos originales"
            for j in range(0,3):
                print neighbours[j]
            print " "

            #Se crean tres nuevos triangulos
            newTriangle1 = Triangle(points[i],conT.p1,conT.p2)
            newTriangle2 = Triangle(points[i],conT.p2,conT.p3)
            newTriangle3 = Triangle(points[i],conT.p3,conT.p1)

            #Se asignan los vecinos correspondientes a cada triangulo, notar que van en orden antihorario
            newTriangle1.setNeighbours(conT.getNeighbourFromEdge(Edge(conT.p1,conT.p2)),newTriangle2,newTriangle3)
            newTriangle2.setNeighbours(newTriangle1,conT.getNeighbourFromEdge(Edge(conT.p2,conT.p3)),newTriangle3)
            newTriangle3.setNeighbours(newTriangle1,newTriangle2,conT.getNeighbourFromEdge(Edge(conT.p3,conT.p1)))

            newTriangles = [newTriangle1,newTriangle2,newTriangle3]

            #Hay que notificar a los vecinos del antiguo triangulo quien queda como vecino ahora

            #if i == 1:
            #    print "antes de notificar"
            #    for j in range(0,len(triangulation)):
            #        print "vecinos de " + str(triangulation[j])
            #        neighbours = triangulation[j].getNeighbours()
            #        for k in range(0,3):
            #            print neighbours[k]
            #        print " "

            #for l in range(0,3):
            #    print "Triangulo nuevo" + str(newTriangles[l])
            #    print map(lambda x: str(x),newTriangles[l].getNeighbours())
            #print " "

            conT.notifyNeighbours(newTriangles)

            #Hay que eliminar el triangulo antiguo
            triangulation.remove(conT)

            #Incluir los nuevos triangulos en la triangulacion
            triangulation = triangulation + newTriangles

            #print "contenido actual de la triangulacion"
            #for k in range(0,len(triangulation)):
            #    print triangulation[k]

            #if i == 3:
            #    print "antes del flip"
            #    for j in range(0,len(triangulation)):
            #        print "vecinos de " + str(triangulation[j])
            #        neighbours = triangulation[j].getNeighbours()
            #        for k in range(0,3):
            #            print neighbours[k]
            #        print " "

            #Legalizar los nuevos triangulos
            #print "triangulacion antes de legalize1"
            #print map(lambda x: str(x),triangulation)
            legalizeEdge(points[i],newTriangle1.getEdgeWithoutPoint(points[i]),newTriangle1,triangulation)
            #print " "

            #print "triangulacion antes de legalize2"
            #print map(lambda x: str(x),triangulation)
            legalizeEdge(points[i],newTriangle2.getEdgeWithoutPoint(points[i]),newTriangle2,triangulation)
            #print " "

            #print "triangulacion antes de legalize3"
            #print map(lambda x: str(x),triangulation)
            legalizeEdge(points[i],newTriangle3.getEdgeWithoutPoint(points[i]),newTriangle3,triangulation)

            #if i == 2:
            #    print "despues del flip"
            #    for j in range(0,len(triangulation)):
            #        print "vecinos de " + str(triangulation[j])
            #        neighbours = triangulation[j].getNeighbours()
            #        for k in range(0,3):
            #            print neighbours[k]
            #        print " "
            #        print " "

        else:
            #El punto se encuentra en una arista
            conT2 = conT.getNeighbourFromEdge(conEdge)
	
            #Encontrar el tercer punto de los triangulos que comparten la arista que contiene al puntp
            pk = conT.getThirdPoint(conEdge)
            pl = conT2.getThirdPoint(conEdge)

	        #Se crean los cuatro nuevos triangulos
            newTriangle1 = Triangle(points[i],conEdge.p2,pk)
            newTriangle2 = Triangle(points[i],pk,conEdge.p1)
            newTriangle3 = Triangle(points[i],conEdge.p1,pl)
            newTriangle4 = Triangle(points[i],pl,conEdge.p2)

            #Se asignan los vecinos correspondientes a cada triangulo, notar que van en orden antihorario
            newTriangle1.setNeighbours(newTriangle4,conT.getNeighbourFromEdge(Edge(conEdge.p2,pk)),newTriangle2)
            newTriangle2.setNeighbours(newTriangle1,conT.getNeighbourFromEdge(Edge(conEdge.p1,pk)),newTriangle3)
            newTriangle3.setNeighbours(newTriangle4,newTriangle2,conT2.getNeighbourFromEdge(Edge(pl,conEdge.p1)))
            newTriangle4.setNeighbours(conT2.getNeighbourFromEdge(Edge(pl,conEdge.p2)),newTriangle1,newTriangle3)

            newTriangles = [newTriangle1,newTriangle2,newTriangle3,newTriangle4]

            #Hay que notificar a los vecinos de los dos triangulos contenedores que hay nuevos triangulos vecinos
            conT.notifyNeighbours(newTriangles)
            conT2.notifyNeighbours(newTriangles)

            #Hay que eliminar los triangulos antiguos
            triangulation.remove(conT)
            triangulation.remove(conT2)

	        #Incluir los nuevos triangulos en la triangulacion
            triangulation = triangulation + newTriangles

	        #Legalizar los nuevos triangulos
            legalizeEdge(points[i],newTriangle1.getEdgeWithoutPoint(points[i]),newTriangle1,triangulation)
            legalizeEdge(points[i],newTriangle2.getEdgeWithoutPoint(points[i]),newTriangle2,triangulation)
            legalizeEdge(points[i],newTriangle3.getEdgeWithoutPoint(points[i]),newTriangle3,triangulation)
            legalizeEdge(points[i],newTriangle4.getEdgeWithoutPoint(points[i]),newTriangle4,triangulation)


	#Eliminar los puntos que conforman al triangulo contenedor de los puntos y las aristas que los conectan
	#AAAAAH, como? xD
    #removeBigTriangle(baseTriangle,triangulation)

    return triangulation

if __name__ == '__main__':
    points = randomPoints(100,100,400)
    #print map(lambda x: str(x),points)

    #points = [Point2D(162,289), Point2D(164,157), Point2D(234,208), Point2D(219,193), Point2D(163,183), Point2D(284,274), Point2D(218,152), Point2D(161,205), Point2D(189,272), Point2D(279,160)]

    #points =[Point2D(100,100),Point2D(100,200),Point2D(200,200),Point2D(200,100),Point2D(300,100),Point2D(300,200),Point2D(400,100),Point2D(400,200),
             #Point2D(100,0),Point2D(200,0),Point2D(300,0),Point2D(400,0)]

    window = Tk()
    frame = Frame(window)
    frame.pack()

    canvas = Canvas(window,width=600,height=400,bg="white")
    triangulation = delaunay(points,canvas)

    #for i in range(0,5):
    #	points[i].draw(canvas)

    for i in range(0,len(triangulation)):
	    triangulation[i].draw(canvas,"blue")

    canvas.pack()
    window.mainloop()

 
	    







