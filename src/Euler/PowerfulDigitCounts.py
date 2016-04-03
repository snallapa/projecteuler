
def checkPower(number):
	power = len(str(number))
	numbedChecked = 0
	for i in xrange(1,number):
		numberChecked = i ** power
		if numberChecked < number:
			continue
		if numberChecked == number:
			return True
		if numberChecked > number:
			return False
	return False

powerList = []
print checkPower(134217728)
for i in xrange(1,1000000000/2):
	if checkPower(i):
		powerList.append(i)

print powerList
print len(powerList)