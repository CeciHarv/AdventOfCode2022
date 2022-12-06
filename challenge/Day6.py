X = [l.strip() for l in open('Day6/data.txt')]

X = X[0]
# print(X)

def repeat(sub):
    for i in sub:
        if sub.count(i) > 1:
            return False
    return True

def makeSubStr(strin, leng):
    for i in range(len(X)-leng):
        subStr = X[i:i+leng]
        if repeat(subStr):
            return (i+leng)
    
print("Part 1:", makeSubStr(X, 4))
print("Part 2:", makeSubStr(X, 14))
