import math, time

primeDictionary = []
def checkPrime(number):
	if number in primeDictionary:
		return True
	if number == 1:
		return False;
	for i in range(2,int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	primeDictionary.append(number)
	return True
def findDivisors(number):
	divisorList = [1]
	for i in xrange(2,number+1):
		if number % i == 0:
			divisorList.append(i)
	return divisorList
def checkGenerating(number):
	divisorList = findDivisors(number)
	for divisor in divisorList:
		if checkPrime(divisor + number/divisor) == False:
			return False
	return True

#assertion
#print checkGenerating(31)
start = time.time()
generatingPrimes = []
for i in xrange(1,100000001):
	if checkPrime(i) == True:
		continue
	if checkGenerating(i):
		generatingPrimes.append(i)

end = time.time()
print end - start
print sum(generatingPrimes)