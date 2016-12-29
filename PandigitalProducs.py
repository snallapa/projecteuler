import itertools
permutations = itertools.permutations(range(1,10))

pandigitalProducts = set([])
for permutation in permutations:
	a = int(str(permutation[0]) + str(permutation[1]))
	b = int(str(permutation[2]) + str(permutation[3]) + str(permutation[4]))
	c = int(str(permutation[5]) + str(permutation[6]) + str(permutation[7]) + str(permutation[8]))
	if a*b == c:
		pandigitalProducts.add(c)
	a = int(str(permutation[0]))
	b = int(str(permutation[1]) + str(permutation[2]) + str(permutation[3]) + str(permutation[4]))
	c = int(str(permutation[5]) + str(permutation[6]) + str(permutation[7]) + str(permutation[8]))
	if a*b == c:
		pandigitalProducts.add(c)
print pandigitalProducts
print sum(pandigitalProducts)