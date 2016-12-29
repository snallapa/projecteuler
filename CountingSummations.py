import time
def partition(maxNumber):
	partitions = [0 for x in xrange(0,maxNumber + 1)]
	partitions[0] = 1
	partitions[1] = 1
	n = 2
	while True:
		for l in xrange(1,n):
			k1 = l*(3*l-1)/2
			k2 = l*(3*l+1)/2
			if k1 > n or k2 > n:
				if k1 <= n:
					partitions[n] = partitions[n] + ((-1)**(l-1))*partitions[n-k1]
				break
			partitions[n] = partitions[n] + ((-1)**(l-1))*partitions[n-k1] + ((-1)**(l-1))*partitions[n-k2] 
		if n == maxNumber:
			return partitions[maxNumber]
			break
		n = n +1

start = time.time()
result = partition(100) - 1
end = time.time()
print result
print (end - start) * 1000