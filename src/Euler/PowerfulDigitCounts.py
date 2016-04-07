import numpy
def checkPower(number):
	power = len(str(number))
	lol = numpy.power(number, 1.0/float(power))
	print lol
	return float(lol).is_integer()

powerList = []
print checkPower(134217728)
'''
for i in xrange(1,1000000000/2):
	if checkPower(i):
		powerList.append(i)
'''
print powerList
print len(powerList)