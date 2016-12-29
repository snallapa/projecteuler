import math, time
def period(n):
	m = 0
	d = 1
	a0 = math.floor(math.sqrt(n))
	a = a0
	period = []
	while a != 2 * a0:
		m = d * a - m
		d = (n - m*m)/d
		a = int(math.floor(float((a0 + m))/d))
		period.append(a)
	return period
start = time.time()
count = 0
for i in xrange(2,10001):
	if math.sqrt(i).is_integer():
		continue
	if len(period(i)) % 2 == 1:
		count = count + 1
end = time.time()
print count
print (end - start) * 1000