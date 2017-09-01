import itertools, math, time

primeDictionary2 = [True for i in range(0,50000)]
primeDictionary2[1] = False
for i in range(2,223):
	for k in range(i*2,50000,i):
		primeDictionary2[k] = False

primeDictionary = []
def checkPrime(number):
	if number in primeDictionary:
		return True
	if number == 1:
		return False;
	for i in range(2,int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	primeDictionary.append(number)
	return True


def primeList(upperBound, lowerbound=3):
    return [x for x in range(lowerbound,upperBound) if primeDictionary2[x]]
def checkConcate(primeList):
    for primeList in itertools.permutations(primeList, 2):
        prime1 = list(primeList)[0]
        prime2 = list(primeList)[1]
        if checkPrime(int(str(prime1) + str(prime2))) == False:
            return False
    return True

def addPrime(currentPrimeList):
    newPrimeList = []
    for prime in primeList(10000, max(currentPrimeList)):
        possibility = currentPrimeList + [prime]
        if checkConcate(possibility):
            newPrimeList.append(possibility)
    return newPrimeList

primes = primeList(100)
start = time.time()
for prime in primes:
	possibilities = [[prime]]
	found = True
	for i in range(4):
	    newPossibilities = []
	    for possibility in possibilities:
	        newPossibilities = newPossibilities + addPrime(possibility)
	    possibilities = newPossibilities
	    if len(possibilities) == 0:
	        found = False
	        break
	if found:
	    print(possibilities)
	    print(sum(possibilities[0]))
	    break
end = time.time()
print(str((end - start) * 1000) + "ms")
