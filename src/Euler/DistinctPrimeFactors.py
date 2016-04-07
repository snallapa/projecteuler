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


num1 = 500
distinctPrimes = set([])
while True:
    num2 = num1 + 1
    num3 = num1 + 2
    num4 = num1 + 3
    num1Factors = primes(num1)
    num2Factors = primes(num2)
    num3Factors = primes(num3)
    num4Factors = primes(num4)
    if len(num1Factors) == 4 and len(num2Factors) == 4 and len(num3Factors) ==4 and len(num4Factors) == 4:
        print num1
        break
    num1 = num1 + 1