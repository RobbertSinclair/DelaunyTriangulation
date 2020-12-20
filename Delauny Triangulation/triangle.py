from point import Point

class Triangle:

    def __init__(self, point1, point2, point3, superTri=False):
        self.points = [point1, point2, point3]
        self.superTri = superTri

    def isSuper(self):
        return self.superTri

    def getTriCoords(self):
        return self.points

    
    def getEdges(self):
        points = self.getTriCoords()
        #Create the edges
        edge1 = [points[0], points[1]]
        edge2 = [points[0], points[2]]
        edge3 = [points[1], points[2]]
        edges = [edge1, edge2, edge3]
        return edges

    
