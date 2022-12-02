import csv

rounds = []
with open("data/data2.txt") as file:
    csv.reader(file)
    for row in file:
        rounds.append(row.replace("\n", ""))
        # print(rounds[-1])

myScore = 0

def findResult(play):
    opponentPlay = play[0]
    myPlay = play[-1]
    pointsEarned = 0

    if opponentPlay == "A":
        if myPlay == "X":
            pointsEarned = 3 + 1
        elif myPlay == "Y":
            pointsEarned = 6 + 2
        else:
            pointsEarned = 3
    elif opponentPlay == "B":
        if myPlay == "Y":
            pointsEarned = 3 + 2
        elif myPlay == "Z":
            pointsEarned = 6 + 3
        else:
            pointsEarned = 1
    elif opponentPlay == "C":
        if myPlay == "Z":
            pointsEarned = 3 + 3
        elif myPlay == "X":
            pointsEarned = 6 + 1
        else:
            pointsEarned = 2
    print(pointsEarned)
    return pointsEarned

def setMyPlay(play):
    opponentPlay = play[0]
    myPlay = play[-1]

    if opponentPlay == "A":
        if myPlay == "X":
            myChoice = play[:-1] + 'Z'
        elif myPlay == "Y": 
            myChoice = play[:-1] + 'X'
        else:
            myChoice = play[:-1] + 'Y'
    elif opponentPlay == "B":
        if myPlay == "X":
            myChoice = play[:-1] + 'X'
        elif myPlay == "Y":
            myChoice = play[:-1] + 'Y'
        else:
            myChoice = play[:-1] + 'Z'
    elif opponentPlay == "C":
        if myPlay == "X":
            myChoice = play[:-1] + 'Y'
        elif myPlay == "Y":
            myChoice = play[:-1] + 'Z'
        else:
            myChoice = play[:-1] + 'X'
    print(myChoice)
    return myChoice

# Solution to Problem 1
for play in rounds:
    myScore += findResult(play)

# print(myScore)


# Solution to Problem 2
myScore2 = 0
for play in rounds:
    myScore2 += findResult(setMyPlay(play))


print(myScore2)