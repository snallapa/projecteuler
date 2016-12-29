
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
    if len(primesList) != 2:
        return 1
    numerator = 1
    denominator = 1
    for prime in primesList:
        numerator = (prime - 1) * numerator
        denominator = prime * denominator
    return n * numerator/denominator

def checkPermutation(num, num2):
    num1List = sorted([int(x) for x in str(num)])
    num2List = sorted([int(x) for x in str(num2)])
    return num1List == num2List

minTotient = 2/float(totient(2))
minN = 2
for n in xrange(3,10000000, 2):
    totientN = totient(n)
    if checkPermutation(n, totientN):
        if float(n)/totientN < minTotient:
            print str(n) + " " + str(totientN)
            minN = n
            minTotient = float(n)/totientN
print minN