import time

primeDictionary = [True for i in range(0,50000000)]
primeDictionary[1] = False
for i in range(2,7072):
	for k in range(i*2,50000000,i):
		primeDictionary[k] = False

def primeList(upperBound):
    return [x for x in range(2,upperBound) if primeDictionary[x]]

start = time.time()
counter = 0
numbers = set([])
for fourth in primeList(int(pow(50000000, .25))):
    primeFourth = pow(fourth, 4)
    for third in primeList(int(pow(50000000, .33333333))):
        primeThird = pow(third, 3)
        for second in primeList(int(pow(50000000, .5))):
            primeSecond = pow(second, 2)
            if primeSecond + primeThird + primeFourth < 50000000:
                numbers.add(primeSecond + primeThird + primeFourth)
end = time.time()
print(len(numbers))
print(str((end - start) * 1000) + "ms")
