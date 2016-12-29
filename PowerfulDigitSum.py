def digitSum(number):
	digitSum = 0
	while number > 0:
		digitSum = digitSum + number%10
		number = number/10
	return digitSum

maxSum = 0
for a in xrange(2,101):
	for b in xrange(2,101):
		number = a ** b
		currentDigitSum = digitSum(number)
		if (currentDigitSum > maxSum):
			maxSum = currentDigitSum
			
print maxSum