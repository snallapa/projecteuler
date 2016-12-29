numberToString = {0: "", 1 : "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 1000: "onethousand"}

numberToNumber = ""
for i in range(1, 1001):
	currentString = numberToString.get(i, None)
	if currentString != None:
		numberToNumber = numberToNumber + currentString
	else:
		currentString = ""
		if i < 100:
			currentString = numberToString.get(i/10 * 10)
			remainingNum = i % 10
			currentString = currentString + numberToString.get(remainingNum)
		else:
			currentString = numberToString.get(i/100) + "hundred"
			print currentString
			remainingNum = i % 100
			if remainingNum != 0:
				if remainingNum < 20:
					currentString = currentString + "and" + numberToString.get(remainingNum, None)
				else:
					currentString = currentString + "and" + numberToString.get(remainingNum/10 * 10)
					remainingNum = remainingNum % 10
					currentString = currentString + numberToString.get(remainingNum)
			
		numberToNumber = numberToNumber + currentString

print len(numberToNumber)