class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def setX(self, x):
        self.x =  x
        self.coords = (self.x, self.y)

    def setY(self, y):
        self.y = y
        self.coords = (self.x, self.y)
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCoords(self):
        return self.coords