# Monopoly Odds Euler 84
import random 

board = [i for i in range(40)]

def drawCommunityChest(currentTile):
    def chooseCard():
        ccCard = random.randrange(1,17)
        if ccCard == 1:
            return 0
        elif ccCard == 2:
            return 10
        return currentTile
    return chooseCard

def drawChanceCard(currentTile):
    def chooseCard():
        chanceCard = random.randrange(1,17)
        railRoads = [5, 15, 25, 35]
        utilities = [12, 28]
        nextRailRoad = railRoads[0]
        for r in railRoads:
            if currentTile < r:
                nextRailRoad = r
                break
        nextUtility = utilities[0]
        for u in utilities:
            if currentTile < u:
                nextUtility = u
                break
        chanceType = {1: 0, 2: 10, 3: 11, 4: 24, 5: 39, 6: 5, 7: nextRailRoad, 8: nextRailRoad, 9: nextUtility, 10:(currentTile - 3) % 40}
        if chanceCard in chanceType:
            return chanceType[chanceCard]
        return currentTile
    return chooseCard

def roll(d1=6, d2=6):
    return random.randrange(1,d1 + 1) + random.randrange(1,d2 + 1)

specialTiles = {
    2: drawCommunityChest(2), 
    7: drawChanceCard(7), 
    17: drawCommunityChest(17), 
    22: drawChanceCard(22), 
    30: lambda: 10, #go to jail
    33: drawCommunityChest(33), 
    36: drawChanceCard(36)
}

landed = {0: 1}
turns = 0
current = 0
while turns < 1000000:
    current = (current + roll(4,4)) % 40
    if current in specialTiles:
        current = specialTiles[current]()
    landed[current] = 1 + landed.get(current, 0)
    turns += 1

percentages = []
for k,v in landed.items():
    percentage = (v/turns) * 100
    percentages.append((k, percentage))

percentages.sort(key=lambda s: s[1], reverse=True)
a = int(percentages[0][0])
b = int(percentages[1][0])
c = int(percentages[2][0])
print("{:02d}{:02d}{:02d}".format(a,b,c))