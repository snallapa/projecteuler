coinPartitions = [0 for x in xrange(0,10000000)]
coinPartitions[0] = 1
coinPartitions[1] = 1
n = 2
while True:
	for l in xrange(1,n):
		k1 = l*(3*l-1)/2
		k2 = l*(3*l+1)/2
		if k1 > n or k2 > n:
			if k1 <= n:
				coinPartitions[n] = coinPartitions[n] + ((-1)**(l-1))*coinPartitions[n-k1]
			break
		coinPartitions[n] = coinPartitions[n] + ((-1)**(l-1))*coinPartitions[n-k1] + ((-1)**(l-1))*coinPartitions[n-k2] 
	if n == 50:
		print coinPartitions[50]
		break
	n = n +1