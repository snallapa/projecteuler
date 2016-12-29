import math

powerList = [1]

for x in xrange(2,100000):
	exponent = 1
	while True:
		power = math.pow(x, exponent)
		if len(str(int(power))) == exponent:
			powerList.append(power)
		else:
			break
		exponent = exponent + 1

print powerList
print len(powerList)