def checkMultiplies(number):
	numberlist = [number]
	numberlist.append(number * 2)
	numberlist.append(number * 3)
	numberlist.append(number * 4)
	numberlist.append(number * 5)
	numberlist.append(number * 6)
	digitList = [len(str(number))]
	setOriginalNumber = set(str(number))
	for num in numberlist:
		if len(str(num)) not in digitList:
			return False
		setNum = set(str(num))
		if setNum != setOriginalNumber:
			return False
	return True

i = 1
numberFound = 0
while (True):
	if checkMultiplies(i):
		numberFound = i
		break
	i = i + 1
print numberFound
