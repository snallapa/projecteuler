
def sharedDigit(num1, num2):
	for char in str(num1):
		if char in str(num2):
			return char
	return None
denom = []
numerator = []
for a in range(1, 100):
	for b in range(1, 100):
		digit = sharedDigit(a, b)
		if digit == None or a%10 == 0:
			continue

		newA = str(a).replace(digit, "")
		newB = str(b).replace(digit, "")
		if not newA or not newB:
			continue
		newA = int(newA)
		newB = int(newB)
		if newA == 0 or newB == 0:
			continue
		if newA/float(newB) == a/float(b) and a/float(b) < 1:
			denom.append(b)
			numerator.append(a)
num = reduce(lambda x, y: x*y, numerator)
dum = reduce(lambda x, y: x*y, denom)
print num
print dum