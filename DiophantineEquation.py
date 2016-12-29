import math, time
def period(n):
	m = 0
	d = 1
	a0 = math.floor(math.sqrt(n))
	a = a0
	period = [int(a0)]
	while a != 2 * a0:
		m = d * a - m
		d = (n - m*m)/d
		a = int(math.floor(float((a0 + m))/d))
		period.append(a)
	return period
def p(n, d):
	periods = period(d)
	p = [0 for i in xrange(0,n + 1)]
	p[0] = periods[0]
	cycle = periods[1:]
	p[1] = periods[0] * periods[1] + 1
	for i in xrange(2, n + 1):
		p[i] = cycle[(i -1) % len(cycle)]*p[i - 1] + p[i-2]
	return p[n]

def solveX(d):
	i = len(period(d)) - 1
	if i%2 == 0:
		return p(i - 1, d)
	else:
		return p(2*i - 1, d)
start = time.time()
maxX = 0
maxD = 0
for i in xrange(2,1001):
	if math.sqrt(i).is_integer():
		continue
	solvedX = solveX(i)
	if (solvedX > maxX):
		maxX = solvedX
		maxD = i
end = time.time()
print maxD
print (end- start) * 1000