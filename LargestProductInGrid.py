numberGrid = open("numberGrid.txt", "r")
array = []
for line in numberGrid:
	array.append(map(int, line.split()))
print array

largestProduct = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
for row in range(len(array) - 3):
	for column in range(len(array[0]) - 3):
		#right
		num1 = array[row][column]
		num2 = array[row][column + 1]
		num3 = array[row][column + 2]
		num4 = array[row][column + 3]
		currentProduct = num1 * num2 * num3 * num4
		if currentProduct > largestProduct:
			largestProduct = currentProduct
		#down
		num1 = array[row][column]
		num2 = array[row + 1][column]
		num3 = array[row + 2][column]
		num4 = array[row + 3][column]
		currentProduct = num1 * num2 * num3 * num4
		if currentProduct > largestProduct:
			largestProduct = currentProduct
		#diagonal left to right
		num1 = array[row][column]
		num2 = array[row + 1][column + 1]
		num3 = array[row + 2][column + 2]
		num4 = array[row + 3][column + 3]
		currentProduct = num1 * num2 * num3 * num4
		if currentProduct > largestProduct:
			largestProduct = currentProduct
		#diagonal right to left plus checks
		if row - 3 > -1 :
			num1 = array[row][column]
			num2 = array[row - 1][column + 1]
			num3 = array[row - 2][column + 2]
			num4 = array[row - 3][column + 3]
			currentProduct = num1 * num2 * num3 * num4
			if currentProduct > largestProduct:
				largestProduct = currentProduct

print 
print largestProduct