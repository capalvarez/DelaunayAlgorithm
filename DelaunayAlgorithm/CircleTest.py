__author__ = 'cata'

def circleTest(a,b,c,d):
    #Decide si una triangulacion local es Delaunay o no; devuelve -1 si el punto d esta dentro del circulo (no cumple
    # condicion) o 1 si cumple
    p11 = a.getX() - d.getX()
    p12 = a.getY() - d.getY()
    p13 = (a.getX()**2 - d.getX()**2) + (a.getY()**2 - d.getY()**2)

    p21 = b.getX() - d.getX()
    p22 = b.getY() - d.getY()
    p23 = (b.getX()**2 - d.getX()**2) + (b.getY()**2 - d.getY()**2)

    p31 = c.getX() - d.getX()
    p32 = c.getY() - d.getY()
    p33 = (c.getX()**2 - d.getX()**2) + (c.getY()**2 - d.getY()**2)

    return p11*(p22*p33 - p32*p23) - p21*(p12*p33 - p32*p13) + p31*(p12*p23 - p13*p22)
