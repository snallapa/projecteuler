from fractions import Fraction, gcd
import time

def primes(n):
    primfac = set([])
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.add(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.add(n)
    return primfac

def totient(n):
    primesList = list(primes(n))
    numerator = 1
    denominator = 1
    for prime in primesList:
        numerator = (prime - 1) * numerator
        denominator = prime * denominator
    return n * numerator/denominator

def generateFractions(n):
	numFractions = 1
	for i in xrange(3, n + 1):
		numFractions = numFractions + totient(i)
	return numFractions
start = time.time()
n = generateFractions(1000000)
end = time.time()
print n
print str((end - start) * 1000) + "ms"