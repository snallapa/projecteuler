from fractions import Fraction

def digitSum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


e = [2]
i = 0
while len(e) < 100:
	e.append(1)
	e.append(2 * (i + 1))
	e.append(1)
	i = i + 1
while not len(e) == 1:
	last = e.pop(-1)
	secondLast = e.pop(-1)
	e.append(secondLast + Fraction(1, last))

print digitSum(e[0].numerator)