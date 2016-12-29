import math

primeDictionary = []
def checkPrime(number):
	if number in primeDictionary:
		return True
	if number == 1 or number%2 == 0:
		return False;
	for i in range(3,int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	primeDictionary.append(number)
	return True
def checkPandigital(n):
	size = len(str(n))
	if (size>9):
		size = 9
	for i in range(1, size+1):
		if str(i) not in str(n):
			return False
	return True
for i in xrange(1000001, 999999999, 2):
	if checkPandigital(i) and checkPrime(i):
		print i