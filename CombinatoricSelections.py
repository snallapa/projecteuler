import math, time

def nCr(n, r):
	numerator = math.factorial(n)
	denominator = math.factorial(r) * math.factorial(n-r)
	return numerator/denominator
start = time.time()
count = 0
for n in xrange(1,101):
	for r in xrange(3,n-3):
		choose = nCr(n, r)
		if choose > 1000000:
			count = count + 1
end = time.time()
print count
print end - start