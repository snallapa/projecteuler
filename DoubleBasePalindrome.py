def checkPalindrome(number):
	return int(str(number)[::-1]) == number

def convertBinary(number):
	return int(bin(number)[2:])

def checkMultiPalindrome(number):
	if checkPalindrome(number) and checkPalindrome(convertBinary(number)):
		return True
	else:
		return False

palindromeList = []
for i in xrange(1,1000000):
	if checkMultiPalindrome(i):
		palindromeList.append(i)

print sum(palindromeList)