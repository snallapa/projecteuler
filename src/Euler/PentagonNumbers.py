import math

def pentagonNumber(n):
	return (n * (3*n-1))/2

def checkPentagon(pn):
	discrim = math.sqrt(24*pn+1)
	root1 = (1+discrim)/6.0
	return root1.is_integer()


minDiff = 1000000000000

for i in xrange(1,10000):
	for j in xrange(1,10000):
		firstPent = pentagonNumber(i)
		secondPent = pentagonNumber(j)
		sumPent = firstPent + secondPent
		diffPent = abs(firstPent - secondPent)
		if diffPent == 0:
			continue
		if checkPentagon(sumPent) and checkPentagon(diffPent):
			if diffPent < minDiff:
				minDiff = diffPent
print minDiff