import math
def chain(n):
	chain = [n]
	newChain = sum([math.factorial(int(i)) for i in str(n)])
	while newChain not in chain:
		chain.append(newChain)
		newChain = sum([math.factorial(int(i)) for i in str(newChain)])
	return chain
count = 0
print
for x in xrange(1,1000000):
	if (len(chain(x))) == 60:
		print x
		count = count + 1
print count
