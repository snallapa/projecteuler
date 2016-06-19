primeDictionary = {}
def primes(n):
    primfac = set([])
    d = 2
    while d*d <= n:
        if primeDictionary.get(n, None) != None:
            primfac.update(primeDictionary.get(n))
            break
        while (n % d) == 0:
            primfac.add(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1 and len(primfac) <2:
       primfac.add(n)
    primeDictionary[n] = primfac
    return primfac

def totient(n):
	count = 1
	primesList = primes(n)
	product = 1
	for prime in primesList:
		product = product*float(1 - 1/float(prime))
	return n*product
def checkPermutation(num, num2):
    return set([int(x) for x in str(num)]) == set([int(x) for x in str(num2)])
min = 2/totient(2)
minN = 2
for n in xrange(2,10000000):
    totientN = totient(n)
    if checkPermutation(n, int(totientN)):
        print n
        if n/totientN < min:

            minN = n
            min = n/totientN
print minN