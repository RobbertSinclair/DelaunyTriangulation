import numpy as np
from point import *
from triangle import *
import matplotlib.pyplot as plt
import random
import math

def buildSuperTriangle(thePoints):
    
    #thePoints = [point.getCoords() for point in thePoints]
    
    
    #Find all the x values and find the maximum and minimum values for x
    x_values = [point[0] for point in thePoints]
    x_max = max(x_values)
    x_min = min(x_values)
    #Find all the y values and find the minimum values for y
    y_values = [point[1] for point in thePoints]
    y_max = max(y_values)
    y_min = min(y_values)
    

    #Draw the rectangle
    
    #Find the midpoint to create the hypoteneuse of the main triangle
    x_midpoint = (x_min + x_max) / 2
    x_length = (x_max - x_min) / 2
    y_length = y_max - y_min
    hypotenuse = math.sqrt(((x_length) ** 2) + ((y_length)**2))
    superPoint1 = ((x_min-x_length)-5, (y_max-y_length)-5)
    superPoint2 = ((x_max+x_length)+5, (y_max-y_length)-5)
    superPoint3 = ((x_max-x_length), y_max+(y_length))
    superTriangle = Triangle(superPoint1, superPoint2, superPoint3, superTri=True)

    return superTriangle

def checkInCircumCircle(theTriangle, thePoint):
    triCoords = theTriangle.getTriCoords()
    pointX, pointY = thePoint
    #Create a matrix containing all of the 
    theArray = np.array(
        [[(triCoords[0][0]-pointX), (triCoords[0][1]-pointY),(triCoords[0][0]-pointX)**2 + (triCoords[0][1]-pointY)**2],
        [(triCoords[1][0]-pointX), (triCoords[1][0]-pointY), (triCoords[1][0]-pointX)**2 + (triCoords[1][1]-pointY)**2],
        [(triCoords[2][0]-pointX), (triCoords[2][1]-pointY), (triCoords[2][0]-pointX)**2 + (triCoords[2][1]-pointY)**2]]
    )
    theDeterminant = np.linalg.det(theArray)
    print(f"The determinant is {theDeterminant}")
    if theDeterminant > 0:
        return True
    else:
        return False

def Triangulation(superTriangle, points):
    triangles = [superTriangle]
    for point in points:
        #print("Loop A has run")
        invalidTriangles = []
        for triangle in triangles:
            #print("Loop B has run")
            if checkInCircumCircle(triangle, point):
                print("The point is in the circumcircle")
                invalidTriangles.append(triangle)
        thePolygon = []
        superEdges = superTriangle.getEdges()
        for triangle in invalidTriangles:
            #print("Loop C has run")
            invalidEdges = triangle.getEdges()
            for otherTriangle in triangles:
                #print("Loop C1 has run")
                if otherTriangle not in invalidTriangles:
                    validEdges = otherTriangle.getEdges()
                    for edge in validEdges:
                        #print("Loop C2 has run")
                        if edge in invalidEdges:
                            thePolygon.append(edge)
        if len(thePolygon) == 0:
            thePolygon = superEdges
        for triangle in invalidTriangles:
            #print("Loop D has run")
            theIndex = triangles.index(triangle)
            triangles.pop(theIndex)
        for edge in thePolygon:
            #print("Loop E has run")
            newTri = Triangle(point, edge[0], edge[1])
            #print(f"newTri is {newTri}")
            triangles.append(newTri)
    trianglesToRemove = []
    for triangle in triangles:
        #print("Loop F has run")
        superTriangleCoords = superTriangle.getTriCoords()
        triangleCoords = triangle.getTriCoords()
        trianglesToRemove = []
        for coords in triangleCoords:
            #print("Loop F1 has run")
            if coords in superTriangleCoords:
                trianglesToRemove.append(triangle)
    #print(triangles)
    #print(trianglesToRemove)
    triangles = removeTriangles(triangles, trianglesToRemove)
    return triangles

def removeTriangles(triangles, trianglesToRemove):
    return [triangle for triangle in triangles if triangle not in trianglesToRemove]

def showTriangulation(triangles):
    for triangle in triangles:
        triEdges = triangle.getEdges()
        for edge in triEdges:
            x_values = [edge[0][0], edge[1][0]]
            y_values = [edge[0][1], edge[1][1]]
            plt.plot(x_values, y_values)
    plt.show()



triPoint1 = Point(0, 0)
triPoint2 = Point(2, 4)
triPoint3 = Point(5, 10)
outPoint1 = Point(1, 1)

triangle = Triangle(triPoint1, triPoint2, triPoint3)
points = [ tuple([random.randint(0,20), random.randint(0,20)]) for i in range(12)]
superTriangle = buildSuperTriangle(points)
triangles = Triangulation(superTriangle, points)
showTriangulation(triangles)

