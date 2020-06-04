#Karan Vombatkere
#May 2020

#IMPORTS
import collections
from hexLib import *

##Class to implement Catan board Hexagonal Tile
Resource = collections.namedtuple("Resource", ["type", "num"])

class hexTile():
    'Class Definition for Catan Board Hexagonal Tile'

    #Object Creation - specify the resource, num, center and neighbor list
    #Center is a point in axial coordinates q, r and neighborList is a list of hexTiles
    #hexIndex is a number from 0-18 specifying the Hex's position
    def __init__(self, hexIndex, hexResource, axialCoords, neighborList=None):
        self.hex = Axial_Hex(axialCoords) #Hex representation of this tile
        self.resource = hexResource
        self.coord = axialCoords
        self.pixelCenter = None #Pixel coordinates of hex as Point(x, y)
        self.index = hexIndex
        self.neighborList = neighborList
        self.robber = False

    #Function to update hex neighbors
    def updateNeighbors(self):  
        return None


    #Function to Display Hex Info
    def displayHexInfo(self):
        print('Index:{}; Hex:{}; Axial Coord:{}'.format(self.index, self.resource, self.coord))
        return None
        

    #Function to display Hex Neighbors
    def displayHexNeighbors(self):
        print('Neighbors:')
        for neighbor in self.neighborList:
            neighbor.displayHexInfo()

        return None


#Class definition of a Vertex
class Vertex():
    
    def __init__(self, pixelCoord, adjHexIndex):
        self.pixelCoordinates = pixelCoord
        self.edgeList = [] #List to store adjacent Vertices
        self.adjacentHexList = [adjHexIndex] #List to store indices of 3 adjacent hexes
        self.edgeState = [False, False, False] #List to determine if a road is built on edge

        self.state = {'Player': None, 'Settlement':False, 'City':False} #Vertex state 
        self.isColonised = False

        self.edgeLength = 80 #Specify for hex size

    #Function to get a Vertex by its pixel coordinates
    def getVertex_fromPixel(self, coords):
        if(self.pixelCoordinates == coords):
            return self

    #Function to return if a vertex v1 is adjacent to another v2
    def isAdjacent(self, v1, v2):
        dist = ((v1.pixelCoordinates.x - v2.pixelCoordinates.x)**2 + (v1.pixelCoordinates.y - v2.pixelCoordinates.y)**2)**0.5
        if(round(dist) == self.edgeLength):
            return True

        return False



#Test Code
# testHex = hexTile(0, Resource('Ore', 8), Point(2,3), [hexTile(2, Resource('Wheat', 11), Point(5,6)), hexTile(3, Resource('Brick', 11), Point(7,4))])
# testHex.displayHexInfo()
# testHex.displayHexNeighbors()