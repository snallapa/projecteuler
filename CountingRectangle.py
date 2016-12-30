import time
def numRectangles(m, n):
	return (m * n * (n+1) * (m+1))/4
start = time.time()
minRect = 10000000
minM = 0
minN = 0
for m in xrange(1,100):
	for n in xrange(1,100):
		numRect = numRectangles(m,n)
		if (numRect > 2000000):
			break
		if (2000000 - numRect) < minRect:
			minRect = 2000000 - numRect
			minM = m
			minN = n
area = minN * minM
end = time.time()
print area
print (end - start) * 1000