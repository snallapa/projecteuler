import math, time
def digitExpansion(n, max):
	digits = []
	digits.append(int(math.floor(math.sqrt(n))))
	remainderPart = n - digits[0] * digits[0]
	remainderPart = remainderPart * 100
	for i in xrange(1,max):
		p = int(''.join(map(str,digits)))
		x = 0
		while (p*20 + x)*x < remainderPart:
			x = x + 1
		x = x-1
		remainderPart = remainderPart - (p*20 + x)*x
		remainderPart = remainderPart * 100
		digits.append(x)
	return digits
start = time.time()
sumRoots = 0
for i in xrange(2,100):
	if math.sqrt(i).is_integer():
		continue
	sumRoots = sumRoots + sum(digitExpansion(i, 100))
end = time.time()
print sumRoots
print (end - start) * 1000