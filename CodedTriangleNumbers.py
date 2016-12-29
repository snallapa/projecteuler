words = open("words.txt", "r")
wordsList = words.read().split(",")

alphabet="abcdefghijklmnopqrstuvwxyz"
def wordScore(name):
	nameList = list(name)
	nameSum = 0
	for character in nameList:
		nameSum = nameSum + alphabet.index(character.lower()) + 1
	return nameSum
def generateTriangleNumbers():
	triangleNumbersList = []
	for i in xrange(1,10000): 
		triangleNumbersList.append((i * (i+1))/2)
	return triangleNumbersList

triangleNumbersList = generateTriangleNumbers()
count = 0
for word in wordsList:
	if wordScore(word) in triangleNumbersList:
		count = count + 1

print count