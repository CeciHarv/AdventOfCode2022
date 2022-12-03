import csv

rucksacks = []
commonItems = []
priorityValue = 0
badges = []
badgeValue = 0

with open("data/data3.txt") as file:
    csv.reader(file)
    for row in file:
        rucksacks.append(row.replace("\n", ""))
        # print(rucksacks[-1])

def defineSackCompartments(sack):
    indexOfCompartment2 = 0
    # print(len(sack))
    indexOfCompartment2 = int(len(sack) / 2)
    # print(indexOfCompartment2)
    return indexOfCompartment2

def findCommonItem(sack):
    indexCompartment2 = defineSackCompartments(sack)
    index = 0
    for item in sack:
        itemToSearchFor = sack[index]
        for i in range(indexCompartment2, len(sack)):
            if itemToSearchFor == sack[i]:
                # print(itemToSearchFor)
                return itemToSearchFor
        index += 1

def findBadge(groupSacks):
    for item in groupSacks[0]:
        itemInSack2 = groupSacks[1].find(item)
        itemInSack3 = groupSacks[2].find(item)
        if (itemInSack2 > -1) and (itemInSack3 > -1):
            return item

def setBadges(allSacks):
    index = 0
    for sack in range(0, len(allSacks), 3 ):
        groupOfElves = []
        groupOfElves.append(allSacks[index])
        groupOfElves.append(allSacks[index + 1])
        groupOfElves.append(allSacks[index + 2])
        badges.append(findBadge(groupOfElves))
        index += 3

def calculatePriority(itemList):
    value = 0
    for item in itemList:
        ascii = ord(item)
        if item.isupper():
            value += ascii - 64 + 26
        else:
            value += ascii - 96
    return value

for sack in rucksacks:
    commonItems.append(findCommonItem(sack))

priorityValue = calculatePriority(commonItems)
setBadges(rucksacks)
badgeValue = calculatePriority(badges)

print(commonItems)
print(priorityValue)
print(badges)
print(badgeValue)
