__author__ = 'cata'

class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def draw(self,canvas):
        canvas.create_oval(self.x,self.y,self.x + 5, self.y + 5, fill = "black")
