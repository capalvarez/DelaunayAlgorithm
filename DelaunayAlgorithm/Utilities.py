__author__ = 'cata'

def sign(number):
    return cmp(number,0)

def findAndRemove(list,triangle):
    if triangle is None:
        return list

    for i in range(0,len(list)):
        if list[i]!=None and triangle.equals(list[i]):
            list.remove(list[i])
            list = list + [triangle]
            break

    return list
