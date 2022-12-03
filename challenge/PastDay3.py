import csv

# Read in the sample file
reportOutput = []
gammaRate = []
gammaRateDec = 0
epsilonRate = []
epsilonRateDec = 0


with open("data/PastSample3.txt") as file:
    csv.reader(file)
    for row in file:
        reportOutput.append(row.replace("\n", ""))
        print(reportOutput[-1])

def findMostCommonBit(index):
    numOfOnes = 0

    for row in reportOutput:
        if int(row[index]) == 1:
            numOfOnes += 1

    if numOfOnes > (len(reportOutput) / 2):
        return 1
    else:
        return 0

def setEpsilonRate(gamma):
    epsilon = []
    for num in gamma:
        if num == 1:
            epsilonRate.append(0)
        else:
            epsilonRate.append(1)

def convertBinToDec(binDigitArray):
    numBinDigits = len(binDigitArray) - 1
    decValue = 0
    for digit in binDigitArray:
        if digit == 1:
            binPlaceValue = pow(numBinDigits, 2)
            decValue += binPlaceValue
        numBinDigits -= 1
    print(decValue)
    return decValue

for index, char in enumerate(reportOutput[0]):
    gammaRate.append(findMostCommonBit(index))

setEpsilonRate(gammaRate)

gammaRateDec = convertBinToDec(gammaRate)
epsilonRateDec = convertBinToDec(epsilonRate)
print(gammaRateDec * epsilonRateDec)

print(gammaRate)
print(epsilonRate)










