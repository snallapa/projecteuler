import time

def generateCollatz(startingNumber, count):
	count += 1
	endCount = collatzDictionary.get(startingNumber, None)
	if startingNumber == 1 or startingNumber == 0:
		return count
	elif endCount != None:
		return count + endCount - 1
	elif startingNumber % 2 == 0:
		return generateCollatz(startingNumber/2, count)
	else:
		return generateCollatz(3*startingNumber + 1, count)
largestCount = 0
startingNumber = 0
collatzDictionary = {}
start = time.time()
for i in range(10000, 1000000):
	currentCount = generateCollatz(i, 0)
	collatzDictionary[i] = currentCount
	if currentCount > largestCount:
		largestCount = currentCount
		startingNumber = i
end = time.time()
print end - start
print startingNumber

