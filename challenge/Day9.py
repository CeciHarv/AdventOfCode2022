from collections import Counter
from tkinter import Y

rawData = [l.strip() for l in open('data/data9.txt')]

class Coordinates:
    def _init_(self, x, y):
        self.x = x
        self.y = y
    def printCoord(self):
        print(self.x, self.y)

moves = [list(l) for l in rawData]
tailVisited = []
headLocation = Coordinates()
headLocation.x = 0
headLocation.y = 0
tailLocation = Coordinates()
tailLocation.x = 0
tailLocation.y = 0

# Functions that will move the head or tail 1 increment
def moveUp(currentCoordinates):
    currentCoordinates.y += 1
    return currentCoordinates.y
    
def moveDown(currentCoordinates):
    currentCoordinates.y -= 1
    return currentCoordinates.y
    
def moveRight(currentCoordinates):
    currentCoordinates.x += 1
    return currentCoordinates.x    

def moveLeft(currentCoordinates):
    currentCoordinates.x -= 1
    return currentCoordinates.x

# Function that will loop through the command and move the head and tail the specified number of times in the specified direction
def moveHeadAndTail(direction, numTimes):
    for movements in range(0, numTimes):
        if(direction == 'U'):
            headLocation.y = moveUp(headLocation)
        elif(direction == 'L'):
            headLocation.x = moveLeft(headLocation)
        elif(direction == 'R'):
            headLocation.x = moveRight(headLocation)
        else:
            headLocation.y = moveDown(headLocation)
        
        moveTail()
        
        # print("Head coord:")
        # headLocation.printCoord()
        # print("Tail coord:")
        # tailLocation.printCoord()
        
# Function to add unique coordinates to the tailVisited list
def addCoordToVisited(tailLocation):
    for coord in tailVisited:
        if(tailLocation.x == coord.x and tailLocation.y == coord.y):
            return
    tempCoord = Coordinates()
    tempCoord.x = tailLocation.x
    tempCoord.y = tailLocation.y
    tailVisited.append(tempCoord)
    
# Function that will move the tail after the head moves
def moveTail():    
    # move right
    if (headLocation.x > tailLocation.x + 1 and headLocation.y == tailLocation.y ):
        tailLocation.x = moveRight(tailLocation)
    # move left
    elif (headLocation.x < tailLocation.x - 1 and headLocation.y == tailLocation.y ):
        tailLocation.x = moveLeft(tailLocation)
    # move up
    elif (headLocation.x == tailLocation.x and headLocation.y > tailLocation.y + 1):
        tailLocation.y = moveUp(tailLocation)
    # move down
    elif (headLocation.x == tailLocation.x and headLocation.y < tailLocation.y - 1):
        tailLocation.y = moveDown(tailLocation)
    # move up and right    
    elif ((headLocation.x > tailLocation.x + 1 and headLocation.y > tailLocation.y) or (headLocation.x > tailLocation.x and headLocation.y > tailLocation.y + 1)):
        tailLocation.y = moveUp(tailLocation)  
        tailLocation.x = moveRight(tailLocation)  
    # move up and left  
    elif ((headLocation.x < tailLocation.x - 1 and headLocation.y > tailLocation.y) or (headLocation.x < tailLocation.x and headLocation.y > tailLocation.y + 1)):
        tailLocation.y = moveUp(tailLocation)  
        tailLocation.x = moveLeft(tailLocation) 
    # move down and right   
    elif ((headLocation.x > tailLocation.x + 1 and headLocation.y < tailLocation.y) or (headLocation.x > tailLocation.x and headLocation.y < tailLocation.y - 1)):
        tailLocation.y = moveDown(tailLocation)  
        tailLocation.x = moveRight(tailLocation)  
    # move down and left    
    elif ((headLocation.x < tailLocation.x - 1 and headLocation.y < tailLocation.y) or (headLocation.x < tailLocation.x and headLocation.y < tailLocation.y - 1)):
        tailLocation.y = moveDown(tailLocation)  
        tailLocation.x = moveLeft(tailLocation)  
    
    addCoordToVisited(tailLocation)

# Function that will go through data and move the head and tail
for move in moves:
    # print(move) 
    moveHeadAndTail(move[0], int(move[-1]))
    
print("Part 1:", len(tailVisited))
