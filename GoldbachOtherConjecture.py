import math

def perfect_sq(n):
    return n == int(math.sqrt(n)) * int(math.sqrt(n))

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

def checkGoldbach(n):
	if checkPrime(n) == True:
		return True
	for i in range(1, n, 2):
		if checkPrime(i) == False:
			continue
		rest = n -i
		rest = rest/2
		if rest > 0:
			if perfect_sq(rest):
				return True
		else:
			continue
	return False

for x in xrange(1,100000, 2):
	checkPrime(x)
for i in range(3, 10000000, 2):
	if checkGoldbach(i) == False:
		print i
		break
