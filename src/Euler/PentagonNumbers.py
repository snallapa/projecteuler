def pentagonNumber(n):
	return (n * (3*n-1))/2

pentagonNumberList = []
for i in xrange(1,10000):
	pentagonNumberList.append(pentagonNumber(i))

minDiff = 1000000000000


for firstPent in pentagonNumberList:
	for seconPent in pentagonNumberList:
		sumPent = firstPent + seconPent
		diffPent = abs(firstPent - seconPent)
		if diffPent == 0:
			continue
		if sumPent in pentagonNumberList and diffPent in pentagonNumberList:
			if diffPent < minDiff:
				minDiff = diffPent
print minDiff