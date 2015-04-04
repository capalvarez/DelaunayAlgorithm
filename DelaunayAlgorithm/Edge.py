__author__ = 'cata'

class Edge:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas,color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = color)
 
    def __str__(self):
        return str(self.p1) + "," + str(self.p2)

    def equals(self,edges):
	if edges.p1.equals(self.p1) and edges.p2.equals(self.p2):
		return True
	elif edges.p1.equals(self.p2) and edges.p2.equals(self.p1):
		return True

	return False


