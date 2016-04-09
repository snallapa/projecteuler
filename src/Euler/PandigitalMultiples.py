def checkPandigital(n):
	size = len(str(n))
	if (size!=9):
		return False
	for i in range(1, size+1):
		if str(i) not in str(n):
			return False
	return True

def checkCreation(n):
	pandigital = []
	for x in xrange(1,10):
		pandigital.append(n*x)
	product = 0
	for num in pandigital:
		product = int(str(product) + str(num))
		if checkPandigital(product):
			return product
	return -1
max = 0
for i in xrange(1,10000):
	pandigital = checkCreation(i)
	if pandigital != -1 and pandigital > max:
		max = pandigital
print max
