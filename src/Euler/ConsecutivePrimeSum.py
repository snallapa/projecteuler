import math
primeDictionary = []
def checkPrime(number):
	if number in primeDictionary:
		return True
	if number == 1 or number%2 == 0:
		return False
	for i in range(3,int(math.sqrt(number)) + 1, 2):
		if i > int(math.sqrt(number)) + 1:
			break
		if number % i == 0:
			return False
	primeDictionary.append(number)
	return True
for i in xrange(1,50000,2):
	checkPrime(i)
consecutivePrime = []
for k in xrange(0, len(primeDictionary)):
	sum = 0
	for l in xrange(0, len(primeDictionary)-k):
		sum = primeDictionary[k+l] + sum
		if sum%2 == 0:
			continue
		if sum > 1000000:
			break
		if checkPrime(sum):
			consecutivePrime.append((sum, l))
	
print max(consecutivePrime, key=lambda x: x[1])