import math, numpy
# doesnt work
def sieve(n):
    """Return a list of the primes below n."""
    prime = [True] * n
    result = [2]
    append = result.append
    sqrt_n = (int(n ** .5) + 1) | 1    # ensure it's odd
    for p in range(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::2*p] = [False] * ((n - p*p - 1) // (2*p) + 1)
    for p in range(sqrt_n, n, 2):
        if prime[p]:
            append(p)
    return result


primeDictionary = sieve(1000000)
def checkPrime(number):
	if number in primeDictionary:
		return True
	if number == 1 or number%2 == 0:
		return False
	for i in range(3,int(math.sqrt(number)) + 1, 2):
		if i > int(math.sqrt(number)) + 1:
			break
		if number % i == 0:
			return False
	primeDictionary.append(number)
	return True
n = 26401
while True:
	count = 0
	for i in xrange(1,n):
		upperRight = 4*i*i -10*i +7
		upperLeft = 4*i*i-8*i+5
		downLeft = 4*i*i-6*i+3
		if upperRight < (n*n + 1) and checkPrime(upperRight):
			count = count + 1
		if upperLeft < (n*n +1) and checkPrime(upperLeft):
			count = count + 1
		if downLeft < (n*n +1) and checkPrime(downLeft):
			count = count + 1
	print 100*count/float(2*n-1)
	if 100*count/float(2*n-1) < 10:
		break
	n = n + 2
print n

