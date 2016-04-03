def calculateDigitPowerSum(number):
	sum = 0
	modifiedNumber = number
	while modifiedNumber > 0:
		sum = sum + (modifiedNumber % 10) ** 5
		modifiedNumber = modifiedNumber/10
		if sum > number:
			return False
	if sum == number:
		return True
	else:
		return False

sum = 0

for i in range(2,1000000):
	if calculateDigitPowerSum(i):
		print i
		sum = sum + i
print sum