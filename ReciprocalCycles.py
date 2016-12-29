def long_divide(n):
	remainders = []
	remainder = 1
	quotient = ""
	while True:
		remainder = remainder*10
		if remainder in remainders:
			remainders.append(remainder)
			size = len(remainders) -1
			first = remainders.index(remainder)
			return size - first
			break
		remainders.append(remainder)
		quotient = str(quotient) + str(remainder/n)
		remainder = remainder%n
		if remainder == 0:
			return 0
		
	return quotient

longestrecurring = 0
j = 0
for i in range(2, 1000):
	recurrence = long_divide(i)
	if  recurrence > longestrecurring:
		longestrecurring = recurrence
		j = i

print longestrecurring
print j