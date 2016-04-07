
def chain(n):
	chain = []
	copyn = n
	while n not in chain:
		chain.append(n)
		if n == 89 or n == 1:
			return n
		digits = []
		while n>0:
			digits.append(n %10)
			n = n/10
		for digit in digits:
			n = n + digit*digit
	chain.append(n)
	return n
count = 0
for i in xrange(10000000):
	if chain(i) == 89:
		count = count + 1
print count