import copy
matrix = []
with open('matrix.txt') as f:
    for line in f:
        int_list = [int(i) for i in line.split(",")]
        matrix.append(int_list)
newMatrix = copy.deepcopy(matrix)
for i in xrange(0, 80):
	for j in xrange(0, 80):
		if i == 0 and j == 0:
			continue
		elif i == 0:
			newMatrix[i][j] = newMatrix[i][j]+ newMatrix[i][j-1]
		elif j == 0:
			newMatrix[i][j] = newMatrix[i][j] + newMatrix[i-1][j]
		else:
			newMatrix[i][j] =  newMatrix[i][j] + min(newMatrix[i-1][j], newMatrix[i][j-1])
print newMatrix