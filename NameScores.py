
alphabet="abcdefghijklmnopqrstuvwxyz"
def nameIndividualScore(name):
	nameList = list(name)
	nameSum = 0
	for character in nameList:
		nameSum = nameSum + alphabet.index(character.lower()) + 1
	return nameSum

namesUnsorted = open("names.txt", "r")
nameList = namesUnsorted.read().split(",")
nameList = sorted(nameList)

totalNameScore = 0
print nameIndividualScore("COLIN")
for i, val in enumerate(nameList):
	thisNameScore = nameIndividualScore(val)*(i+1)
	totalNameScore = totalNameScore + thisNameScore

print totalNameScore