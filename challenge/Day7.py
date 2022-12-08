import cmd
import collections
from tkinter import N

bigSize = []
totalSize = 0
betterTotalSize = 0

X = [l.strip() for l in open('Day7/data.txt')]

cmds = [l.split(" ") for l in X]

fisrtCmd = ['$', 'dir']

class folder:
    def __init__(self, n):
        self.name = n
        
        self.files = {}
        self.folders = {}
        self.size = 0
    

class file:
    def __init__(self, n, s):
        self.name = n
        self.size = s

# for x in cmds:
#     print(x)
    
# def readCmd(cmd):
#     if cmd[0] == "$":
        
def fillFolder(fold, cmds):
    # print(fold.name)
    if len(cmds) == 0:
        return
    if cmds[0][0] == '$' and cmds[0][1] == 'ls':
        cmds.pop(0)
    idx = 0
    while len(cmds) > idx and cmds[idx][0] != '$':
        if cmds[idx][0] == 'dir':
            fold.folders[cmds[idx][1]] = folder(cmds[idx][1])
        elif cmds[idx][0] not in fisrtCmd:
            fold.files[cmds[idx][1]] = file(cmds[idx][1], int(cmds[idx][0]))
        # print(cmds[idx])
        idx += 1
    
    while len(cmds) > idx: #and cmds[idx][0] == '$' and cmds[idx][1] == 'cd' and cmds[idx][2] != '..':
        if idx and cmds[idx][0] == '$' and cmds[idx][1] == 'cd' and cmds[idx][2] != '..':
            folderName = cmds[idx][2]
            idx +=1
            # print("     ",cmds[idx] )
            if len(cmds) < idx:
                return
            idx += fillFolder(fold.folders[folderName], cmds[idx:]) + 1
        elif  cmds[idx][0] == '$' and cmds[idx][1] == 'cd' and cmds[idx][2] == '..':
            idx += 1
            return idx
        else:
            idx += 1
        # idx += 1
    idx +=1
    # print("out of folder")
    # if  cmds[idx][0] == '$' and cmds[idx][1] == 'cd' and cmds[idx][2] == '..':
    #     return
    
    # for 
    return idx
    
   

     
def getSize(fold):
    size = 0
    for f in fold.folders:
        getSize(fold.folders[f])
        size += fold.folders[f].size
        
    for f in fold.files:
        size += fold.files[f].size
    fold.size = size
    
    if size < 100000:
        # print(fold.name, size)
        global totalSize
        totalSize += size
    # if size >= 8381165:
    global betterTotalSize
    betterTotalSize += size
    bigSize.append(size)
        
    
        
elfStuff = folder(cmds[0][2])
cmds.pop(0)

fillFolder(elfStuff, cmds)

getSize(elfStuff)

def printFolder(fold):
    print(fold.name, fold.size)
    
    for i in fold.folders:
        printFolder(fold.folders[i])
    for i in fold.files:
        print(fold.files[i].name, fold.files[i].size)
        
print(totalSize)
print()
# print(elfStuff.size)
# print(30000000 - (70000000 - elfStuff.size))
for t in sorted(bigSize): 
    if t > (30000000 - (70000000 - elfStuff.size)) :  
        print(t)
        break
        
# printFolder(elfStuff)       
# print(elfStuff.folders.keys())
# print(elfStuff.files.keys())
