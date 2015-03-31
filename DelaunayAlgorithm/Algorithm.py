__author__ = 'cata'

from BigTriangle import bigTriangle
from FindTriangle import findTriangle, insideTriangle
from Legalize import legalizeEdge
from Point import Point2D
from Edge import Edge
from Triangle import Triangle 
from Tkinter import *

def delaunay(points,canvas):
    #Encontrar el triangulo inicial de la triangulacion
    baseTriangle = bigTriangle(points,0.3)

    #Incluir el triangulo ficticio en la triangulacion, se debe eliminar posteriormente
    triangulation = [baseTriangle]

    #Ir agregando los puntos a la triangulacion uno o uno
    for i in range(0,5):
        #Tomar un nuevo punto y encontrar el triangulo que lo contiene
        conT = findTriangle(triangulation,points[i])
        [inside,conEdge] = insideTriangle(conT,points[i])
	
        if inside:
            neighbours = conT.getNeighbours()
            #print "vecinos originales"
            #for j in range(0,3):
            #    print neighbours[j]
            #print " "

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

            if i == 1:
                print "antes de notificar"
                for j in range(0,len(triangulation)):
                    print "vecinos de " + str(triangulation[j])
                    neighbours = triangulation[j].getNeighbours()
                    for k in range(0,3):
                        print neighbours[k]
                    print " "

            #print map(lambda x: str(x),newTriangles)
            conT.notifyNeighbours(newTriangles)

            #Hay que eliminar el triangulo antiguo
            triangulation.remove(conT)

            #Incluir los nuevos triangulos en la triangulacion
            triangulation = triangulation + newTriangles


            if i == 1:
                print "antes del flip"
                for j in range(0,len(triangulation)):
                    print "vecinos de " + str(triangulation[j])
                    neighbours = triangulation[j].getNeighbours()
                    for k in range(0,3):
                        print neighbours[k]
                    print " "

            #Legalizar los nuevos triangulos
            legalizeEdge(points[i],newTriangle1.getEdgeWithoutPoint(points[i]),newTriangle1)
            legalizeEdge(points[i],newTriangle2.getEdgeWithoutPoint(points[i]),newTriangle2)
            legalizeEdge(points[i],newTriangle3.getEdgeWithoutPoint(points[i]),newTriangle3)

            #if i == 1:
            #    print "despues del flip"
            #    for j in range(0,len(triangulation)):
            #        print "vecinos de " + str(triangulation[j])
            #        neighbours = triangulation[j].getNeighbours()
            #        for k in range(0,3):
            #            print neighbours[k]
            #         print " "


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

            newTriangles = [newTriangle1,newTriangle2,newTriangle3,newTriangle4]

            #Eliminar los triangulos antiguos
            triangulation.remove(conT)
            triangulation.remove(conT2)
	    
	        #Incluir los nuevos triangulos en la triangulacion
            triangulation = triangulation + newTriangles

	        #Legalizar los nuevos triangulos
            legalizeEdge(points[i],newTriangle1.getEdgeWithoutPoint(points[i]),newTriangle1)
            legalizeEdge(points[i],newTriangle2.getEdgeWithoutPoint(points[i]),newTriangle2)
            legalizeEdge(points[i],newTriangle3.getEdgeWithoutPoint(points[i]),newTriangle3)
            legalizeEdge(points[i],newTriangle4.getEdgeWithoutPoint(points[i]),newTriangle4)


	#Eliminar los puntos que conforman al triangulo contenedor de los puntos y las aristas que los conectan
	#AAAAAH, como? xD
    #removeBigTriangle(baseTriangle,triangulation)

    return triangulation

if __name__ == '__main__':
    #points = randomPoints(20,150,300)
    points =[Point2D(100,100),Point2D(100,200),Point2D(200,200),Point2D(200,100),Point2D(300,100)]

    window = Tk()
    frame = Frame(window)
    frame.pack()

    canvas = Canvas(window,width=600,height=400,bg="white")
    triangulation = delaunay(points,canvas)

    for i in range(0,len(points)):
    	points[i].draw(canvas)

    for i in range(0,len(triangulation)):
	    triangulation[i].draw(canvas,"blue")

    canvas.pack()
    window.mainloop()

 
	    







