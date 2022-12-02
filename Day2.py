import csv

# parse data from txt file
game= []
with open("Day2/data.txt") as file:
    read = csv.reader(file)
    for row in read:
        game.append([])
        
        for r in row:
            game[-1].append(r[0])
            game[-1].append(r[2])
        
def rps(rnd):
    opp = rnd[0]
    me = rnd[1]
    if me == 'X': # rock
        score = 1
        if opp == 'C': # scissors
            score += 6
        if opp == 'A': # rock
            score += 3
        return score
    
    if me == 'Y': # paper
        score = 2
        if opp == 'A': # rock
            score += 6
        if opp == 'B': # paper
            score += 3
        return score
    
    if me == 'Z': # scissors
        score = 3
        if opp == 'B': # paper
            score += 6
        if opp == 'C': #scissors
            score += 3
        return score
    
def shoes(rnd):
    opp = rnd[0]
    me = rnd[1]
    choozin = ''
    
    if me == 'X': # lose
        if opp == 'A': # rock
            choozin = 'Z'
        elif opp == 'B': # paper
            choozin = 'X'
        elif opp == 'C': # scissors
            choozin = 'Y'
        
    
    elif me == 'Y': # Draw
        if opp == 'A': # rock
            choozin = 'X'
        elif opp == 'B': # paper
            choozin = 'Y'
        elif opp == 'C': # scissors
            choozin = 'Z'
    
    elif me == 'Z': # win
        if opp == 'A': # rock
            choozin = 'Y'
        elif opp == 'B': # paper
            choozin = 'Z'
        elif opp == 'C': # scissors
            choozin = 'X'
    return rps([opp, choozin])
    
    
totalScore = 0

# uncomment for part 1
# for r in game:
#     totalScore += rps(r)
    
# uncomment for part 2
for r in game:
    totalScore += shoes(r)
    
print(totalScore)
