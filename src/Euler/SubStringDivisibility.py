import itertools
primes = [2,3,5,7,11,13,17]
permutations = itertools.permutations(range(10))
numbers = []

def checkSubDivisibility(permutation):
	for i in range(7):
		number = int(str(permutation[i+1]) + str(permutation[i+2]) + str(permutation[i+3]))
		if number % primes[i] != 0:
			return False
	return True
for permutation in permutations:
	if permutation[0] == 0:
		continue
	if checkSubDivisibility(permutation):
		number = ''
		for num in permutation:
			number = number + str(num)
		numbers.append(int(number))
print numbers
print sum(numbers)
