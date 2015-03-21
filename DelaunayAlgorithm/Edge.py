__author__ = 'cata'

class Edge:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = "blue")


