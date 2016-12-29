import itertools
def find_cube_root(n):
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo+hi)//2
        if mid**3 < n:
            lo = mid+1
        else:
            hi = mid
    return lo

def is_perfect_cube(n):
    c = int(n**(1/3.))
    return (c**3 == n) or ((c+1)**3 == n)
i = 300
while True:
	print i
	cube = i*i*i
	digits = [int(x) for x in str(cube)]
	permutations = itertools.permutations(digits)
	allPermutations = [int(filter(str.isdigit, repr(x))) for x in permutations]
	combinations = itertools.permutations(allPermutations, 5)
	found = False
	for oneCombination in combinations:
		if len(set([x for x in oneCombination])) != 5:
			continue
		print oneCombination
		correctAssignment = True
		for num in oneCombination:
			if len(str(num)) != len(str(cube)) or not is_perfect_cube(num):
				correctAssignment = False
				break
		if correctAssignment:
			found = True
	if found:
		print i
		break
	i = i +1
