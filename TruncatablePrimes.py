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

def rightToLeftCheck(number):
	while number > 0:
		if checkPrime(number) == False:
			return False
		number = int(number/10)
	return True

def leftToRightCheck(number):
	while number > 0:
		if checkPrime(number) == False:
			return False
		number = number % 10**(len(str(number)) - 1)
	return True

def checkIfContainsEven(number):
	number = str(number)
	if "2" in number or "4" in number or "6" in number or "8" in number:
		return True
	return False
#assertions
#print rightToLeftCheck(3797)
#print leftToRightCheck(3797)

truncatablePrimes = []
start = time.time()
for i in xrange(11,1000000, 2):
	if checkIfContainsEven(i):
		continue
	if rightToLeftCheck(i) and leftToRightCheck(i):
		truncatablePrimes.append(i)
	if len(truncatablePrimes) > 11:
		break
end = time.time()
print end - start
print sum(truncatablePrimes)
print truncatablePrimes