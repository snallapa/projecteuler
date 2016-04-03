import itertools

permutations = itertools.permutations(range(10))

for index, value in enumerate(permutations):
	if (index == 1000000-1):
		print value
		break