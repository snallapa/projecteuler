from fractions import Fraction, gcd

fractionWanted = Fraction(2,5)
for i in xrange(2,1000001):

	if i % 7 == 0:
		newFraction = Fraction(i * 3/7 - 1,i)
	else:
		newFraction = Fraction(i * 3/7, i)
	if newFraction > fractionWanted and newFraction < Fraction(3,7):
		fractionWanted = newFraction
print fractionWanted
