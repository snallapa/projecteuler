import math
import time

primeDictionary = [True for i in xrange(0,1000000)]

def findPrime():
	for prime in xrange(10000,1000000):
		if primeDictionary[prime] == False:
			continue
		for k in range(0,len(str(prime))):
			for l in range(k+1, len(str(prime))):
				for j in range(l+1, len(str(prime))):
					digitList = [int(i) for i in str(prime)]
					primeList = []
					for digit in range(0,10):
						if (k ==0 or l == 0 or j == 0) and digit == 0:
							continue
						digitList[k] = digit
						digitList[l] = digit
						digitList[j] = digit
						newPrime = int("".join(str(x) for x in digitList))

						if primeDictionary[newPrime] == True:
							primeList.append(newPrime)
					if len(primeList) == 8:
						return min(primeList)
start = time.time()
primeDictionary[1] = False
for i in xrange(2,1001):
	for k in xrange(0,1000000,i):
		primeDictionary[k] = False
print findPrime()
end = time.time()
print (end - start)*1000.0

