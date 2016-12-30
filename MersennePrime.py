import math, time
start = time.time()
mod = int(math.pow(10,10))
mersenne = 28433
for i in xrange(0,7830457):
	mersenne = (mersenne * 2) % mod
mersenne = mersenne + 1
end = time.time()
print mersenne
print (end - start) * 1000
