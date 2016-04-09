import math, itertools
primeDictionary = []
def checkPrime(number):
	if number in primeDictionary:
		return True
	if number == 1 or number%2 == 0:
		return False;
	for i in range(3,int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	primeDictionary.append(number)
	return True

def checkSequence(sequence):
	if sequence[2] == sequence[1] or sequence[2] == sequence[0] or sequence[0] == sequence[1]:
		return False
	if checkPrime(sequence[1]) == False or checkPrime(sequence[2]) == False or checkPrime(sequence[0]) == False:
		return False
	if not sequence[2] - sequence[1] == sequence[1]-sequence[0]:
		return False
	return True

works = []
for i in xrange(1000,10000):
	if checkPrime(i) == False:
		continue
	iterations = itertools.permutations(int(x) for x in str(i))
	permutations = []
	for iter in iterations:
		permutations.append(int(''.join(str(x) for x in iter)))
	sequences = itertools.permutations(permutations, 3)
	for sequence in sequences:
		if checkSequence(sequence):
			works.append(sequence)
print works
