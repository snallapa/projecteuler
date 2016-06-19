from fractions import Fraction, gcd

fractionWanted = Fraction(2,5)
for i in xrange(2,1000001):
	for j in xrange(1,i):
		if gcd(j,i) != 1:
			continue
		if Fraction(j,i) > fractionWanted and Fraction(j,i) < Fraction(3,7):
			fractionWanted = Fraction(j,i)
	print i
print fractionWanted
