def calculateDigitPowerSum(number):
	sum = 0
	modifiedNumber = number
	while modifiedNumber > 0:
		sum = sum + (modifiedNumber % 10) ** 5
		modifiedNumber = modifiedNumber/10
		if sum > number:
			break
	return sum

sum = 0

for i in range(10000000,1000000000):
	if calculateDigitPowerSum(i) == i:
		print i
		sum = sum + i
print sum