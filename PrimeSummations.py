import time
primeSummations = [0,0,1,1]

primeDictionary = [True for i in range(0,100000)]
primeDictionary[1] = False
for i in range(2,316):
    for k in range(i*2,100000,i):
        primeDictionary[k] = False

def primeList(upperBound, lowerbound=2):
    return [x for x in range(lowerbound,upperBound) if primeDictionary[x]]
print(primeList(5))

primes = primeList(80000)
def sort(s):
    return ''.join(sorted(s))

start = time.time()
combs = {}
combs[0] = [()]
def primeSums(n):
    if combs.get(n, None) != None:
        return combs[n]
    current = []
    for prime in primes:
        if prime > n:
            break
        left = n - prime
        possibles = primeSums(left)
        for possible in possibles:
            newp = list(possible) + [prime]
            newp = tuple(sorted(newp))
            current.append(newp)
    current = list(set(current))
    combs[n] = current
    return current

#print(primeSums(26))
n = 10
while True:
    if len(primeSums(n)) > 5000:
        print(n)
        end = time.time()
        print((end - start) * 1000)
        break
    n += 1
