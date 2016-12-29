import time

def isPalindrome(number):
	return str(number) == str(number)[::-1]

def reverseNumber(number):
	return int(str(number)[::-1])

def checkLychrel(number):
	for x in xrange(1,51):
		nextNumber = number + reverseNumber(number)
		if isPalindrome(nextNumber):
			return False
		number = nextNumber
	return True
# assertion
# print checkLychrel(4994)
# print isPalindrome(1331)
# print reverseNumber(4555)
start = time.time()
lychrelNumbers = []

for i in xrange(1,10000):
	if checkLychrel(i):
		lychrelNumbers.append(i)
end = time.time()
print end - start
print len(lychrelNumbers)