powerList = []

for a in xrange(2, 101):
	for b in xrange(2, 101):
		powerList.append(a ** b)
print len(set(powerList))