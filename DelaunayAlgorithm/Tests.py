__author__ = 'Cata'

from Tkinter import *
from BigTriangle import bigTriangle, findCorners
from Point import Point2D
from Triangle import Triangle
from Edge import Edge
from FindTriangle import inTriangle
from CircleTest import circleTest
from Legalize import flipEdge

#Prueba de BigTriangle e inTriangle
points = [Point2D(20,20),Point2D(10,14),Point2D(15,10),Point2D(8,10),Point2D(23,32),Point2D(40,20),
          Point2D(12,12),Point2D(30,34),Point2D(10,20),Point2D(17,34),Point2D(24,30)]
triangle = bigTriangle(points,0.15)

(up,down,right,left) = findCorners(points)

window = Tk()

frame = Frame(window)
frame.pack()

canvas = Canvas(window,width=600,height=400,bg="white")
#triangle.draw(canvas)

#for i in range(0,len(points)):
 #  points[i].draw(canvas)

#for i in range(0,len(points)):
  #  print inTriangle(triangle,points[i])

point = Point2D(100,100)
#point.draw(canvas)

print inTriangle(triangle,point)

#Prueba de CircleTest y flipEdge
points = [Point2D(100,100),Point2D(100,200),Point2D(200,200),Point2D(180,120),Point2D(220,80)]
t1 = Triangle(points[0],points[1],points[2])
t2 = Triangle(points[2],points[3],points[0])

t1.setNeighbours(t2,None,None)
t2.setNeighbours(None,None,t1)

#t1.draw(canvas)
#t2.draw(canvas)

#print circleTest(points[0],points[1],points[2],points[3])
#print circleTest(points[0],points[1],points[2],points[4])

newTriangles = flipEdge(t1,t2,Edge(points[0],points[2]))

newTriangles[0].draw(canvas)
newTriangles[1].draw(canvas)

canvas.pack()

window.mainloop()

