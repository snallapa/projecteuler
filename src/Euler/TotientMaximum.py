
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
	count = 1
	primesList = primes(n)
	product = 1
	for prime in primesList:
		product = product*float(1 - 1/float(prime))
	return n*product

max = 0
maxN = 0

for x in xrange(1,1000000):
	if x/float(totient(x)) > max:
		maxN = x
		max = x/float(totient(x))
print maxN