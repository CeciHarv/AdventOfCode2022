import ast
from enum import Enum, IntEnum
from turtle import right
import functools


X = [l.strip() for l in open('Day13/data.txt')]
# print(X)
Q = []

data_pairs = []
for line in ('\n'.join(X)).split('\n\n'):
    # print(line)
    # print()
    data_pairs.append(''.join(line).split('\n'))
    
# print(data_pairs[0])   

pairs = []

def makePacket(packetStr):
    pack = ast.literal_eval(packetStr)
    
    
    
    return pack

for pair in data_pairs:
    pairs.append([])
    for packet in pair:
        pairs[-1].append(makePacket(packet))
        
    

# for pair in pairs:
#     for packet in pair:
#         print(packet)
        
#     print()

LEFT = 0
RIGHT = 1

# p = enum.Enum('LOWER', 'HIGHER', 'EVEN')

class p(IntEnum):
    LOWER = -1
    HIGHER = 1
    EVEN = 0
    
# print(len(pairs[-1][-1][1][1][1][1][1]))


def comparePackets(pairL, pairR):
    # print(pairL)
    # print(pairR)
    # print()
    for i in range(max(len(pairL), len(pairR))):
        if(i < len(pairL) and i < len(pairR)):
            if isinstance(pairL[i], int) and isinstance(pairR[i], int):
                if pairL[i] > pairR[i]:
                    # print('F')
                    return p.HIGHER
                elif pairL[i] < pairR[i]:
                    # print('T')
                    return p.LOWER
            elif isinstance(pairL[i], int):
                if p.EVEN != comparePackets([pairL[i]], pairR[i]):
                    return comparePackets([pairL[i]], pairR[i])
            elif isinstance(pairR[i], int):
                if p.EVEN != comparePackets(pairL[i], [pairR[i]]):
                    return comparePackets(pairL[i], [pairR[i]])
            else:
                if p.EVEN != comparePackets(pairL[i], pairR[i]):
                    return comparePackets(pairL[i], pairR[i])
        elif 0 == len(pairL) and 0 != len(pairR):
            return p.LOWER
        elif 0 != len(pairL) and 0 == len(pairR):
            return p.HIGHER
        elif(i >= len(pairR)):
            # print('F')
            return p.HIGHER
        elif(i >= len(pairL)):
            # print('T')
            return p.LOWER
    # print('T')
    return p.EVEN

# comparePackets(pairs[0])
totalSum = 0

for id, pair in enumerate(pairs):
    if comparePackets(pair[0], pair[1]) == p.LOWER:
        # print(id+1)
        totalSum += (id +1)
    # print(id+1)
        
print("PART 1:", totalSum)

packets = []
for pair in pairs:
    for pack in pair:
        packets.append(pack)
    
packets.append([[2]])
packets.append([[6]])

sorted_l = sorted(packets, key=functools.cmp_to_key(comparePackets))


decoder = 1

for id, pack in enumerate(sorted_l):
    if pack == [[2]]:
        decoder *= (id + 1)
    if pack == [[6]]:
        decoder *= (id + 1)
        break
    # print(id,pack)
print("PART 2:", decoder)    

    
