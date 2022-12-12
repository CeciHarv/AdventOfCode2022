x = [l.strip() for l in open('data/sample9.txt')]

class Coordinates:
    def _init_(self, x, y):
        self.x = x
        self.y = y

moves = [list(l) for l in x]
tailVisited = []
headLocation = Coordinates()
headLocation.x = 0
headLocation.y = 0
tailLocation = Coordinates()
tailLocation.x = 0
tailLocation.y = 0
tailVisited.append(tailLocation)

# Functions that will move the head or tail 1 increment
def moveUp(currentCoordinates):
    currentCoordinates.y += 1
    
def moveDown(currentCoordinates):
    currentCoordinates.y -= 1
    
def moveRight(currentCoordinates):
    currentCoordinates.x += 1

def moveLeft(currentCoordinates):
    currentCoordinates.x -= 1

# Function that will loop through the command and move the head and tail
def moveHead(direction, numTimes):
    for movements in range(0, numTimes):
        if(direction == 'U'):
            moveUp(headLocation)
        elif(direction == 'L'):
            moveLeft(headLocation)
        elif(direction == 'R'):
            moveRight(headLocation)
        else:
            moveDown(headLocation)
    
# Function that will move the tail after the head moves
def moveTail():    
    # move right
    if (headLocation.x > tailLocation.x + 1 and headLocation.y == tailLocation.y ):
        moveRight(tailLocation)
    # move left
    elif (headLocation.x < tailLocation.x - 1 and headLocation.y == tailLocation.y ):
        moveLeft(tailLocation)
    # move up
    elif (headLocation.x == tailLocation.x and headLocation.y > tailLocation.y + 1):
        moveUp(tailLocation)
    # move down
    elif (headLocation.x == tailLocation.x and headLocation.y < tailLocation.y - 1):
        moveDown(tailLocation)
    # move up and right    
    elif (headLocation.x > tailLocation.x and headLocation.y > tailLocation.y):
        moveUp(tailLocation)  
        moveRight(tailLocation)  
    # move up and left  
    elif (headLocation.x < tailLocation.x and headLocation.y > tailLocation.y):
        moveUp(tailLocation)  
        moveLeft(tailLocation) 
    # move down and right   
    elif (headLocation.x > tailLocation.x and headLocation.y < tailLocation.y):
        moveDown(tailLocation)  
        moveRight(tailLocation)  
    # move down and left    
    elif (headLocation.x < tailLocation.x and headLocation.y < tailLocation.y):
        moveDown(tailLocation)  
        moveLeft(tailLocation)  
    
    tailVisited.append(tailLocation)

# Function that will determine if the tail has already visited that space

# Function that will append the new Tail location to the visited list


print(headLocation.x, headLocation.y)
moveHead(moves[0][0], int(moves[0][-1]))
print(headLocation.x, headLocation.y)
