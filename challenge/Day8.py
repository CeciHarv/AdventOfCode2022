X = [l.strip() for l in open('Day8/data.txt')]

data = [list(l) for l in X]
trees = []
for i in data:
    trees.append([int(j) for j in i])

numTreesVisible = 0

def foundVisible(row, col):
    if row == 0 or row == len(trees):
        return True
    if col == 0 or col == len(trees[0]):
        return True
    
    isVisible = True
    
    # Rows
    # from left
    for i in range(0, col):
        if trees[row][i] >= trees[row][col]:
            isVisible = False
            break 
    if isVisible:
        return isVisible
    
    # from right
    isVisible = True
    for i in range(len(trees[row])-1, col, -1):
        if trees[row][i] >= trees[row][col]:
            isVisible = False
            break
    if isVisible:
        return isVisible
    
    # Cols
    # from top
    isVisible = True
    for i in range(0, row):
        if trees[i][col] >= trees[row][col]:
            isVisible = False
            break 
    if isVisible:
        return isVisible
    
    # from bottom
    isVisible = True
    for i in range(len(trees)-1, row, -1):
        if trees[i][col] >= trees[row][col]:
            isVisible = False
            break
    if isVisible:
        return isVisible
    
    return isVisible

for row, treeRow in enumerate(trees):
    for col, tree in enumerate(treeRow):
        if foundVisible(row, col):
            numTreesVisible += 1
           
print("Part 1:",numTreesVisible)

visibleScore = []

def getVisibilityScore(row, col):
    up = 0
    down = 0
    left = 0
    right = 0
    
    # Rows
    # from left
    for i in range(col-1, -1, -1):
        left += 1
        if trees[row][i] >=  trees[row][col]:
            break 
    
    # from right
    for i in range(col + 1, len(trees[row])):
        right += 1
        if trees[row][i] >= trees[row][col]:
            break
    
    # Cols
    # from top
    for i in range(row -1, -1, -1):
        up += 1
        if trees[i][col] >= trees[row][col]:
            break 
    
    # from bottom
    for i in range(row+1, len(trees)):
        down += 1
        if trees[i][col] >= trees[row][col]:
            break
    
    return left * right * up * down

for row, treeRow in enumerate(trees):
    for col, tree in enumerate(treeRow):
        visibleScore.append(getVisibilityScore(row, col))
         
print("Part 2:", sorted(visibleScore)[-1])
