__author__ = 'Cata'

from Tkinter import *
from BigTriangle import bigTriangle, findCorners
from Point import Point2D

points = [Point2D(200,200),Point2D(100,145),Point2D(150,100),Point2D(80,100),Point2D(234,325),Point2D(400,200),
          Point2D(120,120),Point2D(300,345),Point2D(100,200),Point2D(175,345),Point2D(245,300)]
triangle = bigTriangle(points,0.15)

corners = findCorners(points)

window = Tk()

frame = Frame(window)
frame.pack()

canvas = Canvas(window,width=600,height=400,bg="white")
triangle.draw(canvas)

for i in range(0,len(points)):
   points[i].draw(canvas)

canvas.pack()

window.mainloop()

