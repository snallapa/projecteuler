import math

primeDictionary = []
def checkPrime(number):
	if number < 0:
		return False
	if number in primeDictionary:
		return True
	if number == 1:
		return False;
	for i in range(2,int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	primeDictionary.append(number)
	return True

for x in xrange(1,10000):
	checkPrime(x)

maxA = 0
maxB = 0
maxSequence = 0
for a in range(-1000,1000):
	for b in range(-1000,1000):
		n = 0
		sequence = 0
		while True:
			if checkPrime(n*n + a*n + b):
				n = n + 1
				sequence = sequence + 1
			else:
				break
		if sequence > maxSequence:
			maxA = a
			maxB = b
			maxSequence = sequence
print maxA*maxB
print maxA 
print maxB