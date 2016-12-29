#not optimized
def triangular(n):
	return (n*(n+1))/2
def pentagonal(n):
	return (n * (3*n-1))/2
def hexagonal(n):
	return n*(2*n-1)


triangularList = []
pentagonalList = []
hexagonalList = []
for i in xrange(2,100000):
	triangleN = triangular(i)
	pentagonalN = pentagonal(i)
	hexagonalN = hexagonal(i)
	triangularList.append(triangleN)
	pentagonalList.append(pentagonalN)
	hexagonalList.append(hexagonalN)
	if triangleN in pentagonalList and triangleN in hexagonalList:
		print triangleN