def sumOfProperDivisors(number):
	divisorSum = 0
	for x in range(1, number):
		if number % x == 0:
			divisorSum = divisorSum + x
	return divisorSum

amicableNumberList = []

print sumOfProperDivisors(220) #assertion

for i in range(1,10000):
	amicableNumber = sumOfProperDivisors(i)
	sumOfAmicable = sumOfProperDivisors(amicableNumber)
	if sumOfAmicable == i and amicableNumber != i:
		amicableNumberList.append(i)
		amicableNumberList.append(sumOfAmicable)
print sum(amicableNumberList)/2
