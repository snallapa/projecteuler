import time

def productOfStringDigits(digits):
	product = 1
	for i in digits:
		i = int(i)
		product = product * i
	return product

digits = []
champernowne = ""
count = 0
start = time.time()
for i in xrange(0, 1000001):
	if len(champernowne) > 10**count:
		digits.append(champernowne[10**count])
		count = count + 1
	champernowne = champernowne + str(i)
end = time.time()
print end - start
print digits
print productOfStringDigits(digits)