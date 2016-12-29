import time
# Very long solution not the most optimal way
def checkAbundant(number):
	divisorSum = 0
	for x in range(1, number):
		if number % x == 0:
			divisorSum = divisorSum + x
			if divisorSum > number:
				return True
	return False

def checkIfSumOfAbundant(number):
	for i in abundantList:
		checkSum = number - i
		if checkSum < 1:
			continue
		if checkSum in abundantList:
			return True
	return False

abundantList = []

for i in xrange(1, 28124):
	if checkAbundant(i):
		abundantList.append(i)
notSum = []
for x in xrange(1,28124):
	if checkIfSumOfAbundant(x) == False:
		notSum.append(x)
print sum(notSum)