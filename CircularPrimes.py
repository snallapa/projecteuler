
import math

primeDictionary = []
def checkPrime(number):
	if number in primeDictionary:
		return True
	if number == 1:
		return False;
	for i in xrange(2,int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	primeDictionary.append(number)
	return True

def circulateNumber(number):
	number = str(number)
	modifiedNumber = number[1:] + number[0:1]
	return modifiedNumber


def checkCircularPrime(number):
	if checkPrime(number) == False:
		return False
	number = str(number)
	modifiedNumber = circulateNumber(number)
	while modifiedNumber != number:
		if checkPrime(int(modifiedNumber)) == False:
			return False
		modifiedNumber = circulateNumber(modifiedNumber)
	return True

print checkCircularPrime(101)
circularNumberList = [2]
for i in xrange(3,100, 2):
	if i % 5 == 0:
		continue
	if checkPrime(i) == False:
		continue
	if checkCircularPrime(i):
		circularNumberList.append(i)
print circularNumberList
print len(circularNumberList)



