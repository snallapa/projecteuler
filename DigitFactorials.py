import math

def sumOfFactorails(number):
	modifiedNumber = number
	numberSum = 0
	while modifiedNumber > 0:
		numberSum = numberSum + math.factorial(modifiedNumber%10)
		modifiedNumber = modifiedNumber/10
		if (numberSum > number):
			return False
	if numberSum == number:
		return True
	else:
		return False

#assertion
print sumOfFactorails(146)

factorialList = []

for i in xrange(3,1000000):
	if sumOfFactorails(i) == True:
		factorialList.append(i)

print sum(factorialList)