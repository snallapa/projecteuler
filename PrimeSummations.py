primeSummations = [0,0,1,1]

primeDictionary = [True for i in range(0,100000)]
primeDictionary[1] = False
for i in range(2,316):
	for k in range(i*2,100000,i):
		primeDictionary[k] = False

def primeList(upperBound, lowerbound=2):
    return [x for x in range(lowerbound,upperBound) if primeDictionary[x]]
print(primeList(5))
number = 4
while True:
	numberOfWays = 0
	numbersChecked = {}
	for prime in primeList(number):
		numberToCheck = number - prime
		if numbersChecked.get(prime, False) or not primeDictionary[numberToCheck]:
			continue
		numberOfWays = numberOfWays + primeSummations[numberToCheck]
		numbersChecked[numberToCheck] = True
	if primeDictionary[number]:
		numberOfWays = numberOfWays + 1
	primeSummations.append(numberOfWays)
	number = number + 1
	print("on number: {} and numberOfWays was {}".format(number, numberOfWays))
	if numberOfWays > 5000:
		break
