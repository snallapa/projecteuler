# not an optimized method by far probably my worst one
import time

def checkRightTriangle(a, b ,c):
	return a**2 + b**2 == c**2

def generateRightTriangle(p):
	listTriangles = []
	for a in xrange(1,p):
		for b in xrange(1,p-a):
			c = p - a - b
			if c < 0:
				continue
			if c + b < a:
				continue
			if b + a < c:
				continue
			if a + c < b:
				continue
			if checkRightTriangle(a,b,c):
				setTriangle = set([a,b,c])
				if setTriangle not in listTriangles:
					listTriangles.append(setTriangle)
	return listTriangles
#assertion
#print generateRightTriangle(120)
indexP = 0
longestCount = 0
start = time.time()
for i in xrange(1,1001):
	currentCount = len(generateRightTriangle(i))
	if currentCount > longestCount:
		indexP = i
		longestCount = currentCount
end = time.time()
print end - start
print indexP
