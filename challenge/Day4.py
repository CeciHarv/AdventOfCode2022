import csv
import re

rawData = []
elfCleaningAssignments = []
numOfDuplicateAssignments = 0
numOfOverlapAssignments = 0

with open("data/data4.txt") as file:
    csv.reader(file)
    for row in file:
        rawData.append(row.replace("\n", ""))
        # print(rawData[-1])
        # Split input by commas and dashes 
        elfCleaningAssignments.append(re.split("[ ,| -]", rawData[-1]))


# convert to int as it is entered into final array
index = 0
for pair in elfCleaningAssignments:
    elfCleaningAssignments[index] = [int(j) for j in pair]
    index += 1
    
# print(elfCleaningAssignments)
    
def findDuplicateOccurances():
    tempNum = 0
    for pair in elfCleaningAssignments:
        if ((pair[0] <= pair[2]) and (pair[1] >= pair[3])) or ((pair[0] >= pair[2]) and (pair[1] <= pair[3])):
            tempNum += 1
            # print("Overlap Found: " + str(pair))
    return tempNum

def findOverlapOccurances():
    tempNum = 0
    for pair in elfCleaningAssignments:
        if (pair[0] <= pair[3] and pair[2] <= pair[1]):
            tempNum += 1
            # print("Overlap Found: " + str(pair))
    return tempNum        
        
# Puzzle 1: How many pairs of assignments are there where one completely encompases the other assignment? 
numOfDuplicateAssignments += findDuplicateOccurances()       
print(numOfDuplicateAssignments) 

# Puzzle 2: How many pairs of assignments are there where the two assignments overlap each other?
numOfOverlapAssignments += findOverlapOccurances()
print(numOfOverlapAssignments)
    
