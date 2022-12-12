from re import T
from typing import final


X = [l.strip() for l in open('Day12/data.txt')]

data = [list(l) for l in X]
maze = []
for i in data:
    maze.append([[j,False] for j in i])
    
def print2d(arr):
    for row in arr:
        for x in row:
            if(x[1] == False):
                print(x[0], sep='', end='')
            else:
                print(".", sep='', end='')
                
        print()
    print()

# print2d(maze)

def findStartAndEnd(m):
    for idY, row in enumerate(m):
        for idX, col in enumerate(row):
            if(col[0] == 'S'):
                s =  (idX, idY)
            if col[0] == 'E':
                e =  (idX, idY)
    return s,e
            
startCoor, endCoor = findStartAndEnd(maze)
# print(startCoor)
print(endCoor)

def checkBounds(numRows, numCols, coor):
    if coor[1] >= numRows or coor[1] < 0:
        return False
    if coor[0] >= numCols or coor[0] < 0:
        return False
    return True
   
def validStep(now, future, step):
    if(ord(now)+step >= (ord(future))):
        return True
    return False 

def maybeMoveHere(m, coor, future, step):
    if (checkBounds(len(m), len(m[0]), future)):
        if m[future[1]][future[0]][1] == False:
            if(validStep(coor[0], m[future[1]][future[0]][0], step)):
                return True
    return False

def navigate(m, endCoor, step):
    # print2d(m)
    if(m[endCoor[1]][endCoor[0]][1]):
        return 0
    
    newM = []
    
    for r in m:
        newM.append([])
        for x in r:
            newM[-1].append([x[0],x[1]])
    
    for idY, r in enumerate(m):
        for idX, x in enumerate(r):
            if x[1] == True:
                tempCoor = (idX, idY+1) 
                if(maybeMoveHere(m, x, tempCoor, step)):
                    newM[idY+1][idX][1] = True
                tempCoor = (idX, idY-1) 
                if(maybeMoveHere(m, x, tempCoor, step)):
                    newM[idY-1][idX][1] = True
                tempCoor = (idX-1, idY) 
                if(maybeMoveHere(m, x, tempCoor, step)):
                    newM[idY][idX-1][1] = True
                tempCoor = (idX+1, idY) 
                if(maybeMoveHere(m, x, tempCoor, step)):
                    newM[idY][idX+1][1] = True
                    
    return 1 + navigate(newM, endCoor, step)
            
    
    # # Move up
    # tempCoor = (coor[0], coor[1]-1) 
    # if tempCoor != fromCoor and (checkBounds(len(m), len(m[0]), tempCoor)):
    #     if(validStep(coor, tempCoor, step)):
            
        
    
# def historyMap(m):
#     goodMap = []
#     for r in m:
#         goodMap.append([[j,False] for j in r]) 
#     return goodMap
        
# gMaze = historyMap(maze)

# print2d(maze)
maze[startCoor[1]][startCoor[0]][1] = True
maze[startCoor[1]][startCoor[0]][0] = 'a'
maze[endCoor[1]][endCoor[0]][0] = 'z'
# print2d(maze)
        
print("STEP 1:", navigate(maze, endCoor, 1))
        
# print2d(maze)

maze[startCoor[1]][startCoor[0]][1] = False

allPath = []
count = 0
for idY, r in enumerate(maze):
    if r[0][0] == 'a':
        maze[idY][0][1] = True
        allPath.append(navigate(maze, endCoor, 1))
        allPath.sort()
        maze[idY][0][1] = False
        count += 1
        print(count, allPath)
        
# maze[idY][0][1] = True
# allPath.append(navigate(maze, endCoor, 1))
        
            
            
allPath.sort()
print("STEP 2:", allPath[0])
            

