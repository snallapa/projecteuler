from fractions import Fraction
fractionDictionary = [0 for x in xrange(0,1001)]
fractionDictionary[1] = 1/float(2)
def squarerootConvergence(n):
	if n == 1:
		return Fraction(1,2)
	if fractionDictionary[n] != 0:
		return fractionDictionary[n]
	nthTerm = Fraction(1, 2+ squarerootConvergence(n-1))
	fractionDictionary[n] = nthTerm
	return nthTerm
count = 0

for i in xrange(1,1000):
	estimationFraction = 1+ squarerootConvergence(i)
	if len(str(estimationFraction.numerator)) > len(str(estimationFraction.denominator)):
		count += 1
print count