import copy, time
matrix = []
with open('matrix3.txt') as f:
    for line in f:
        int_list = [int(i) for i in line.split(",")]
        matrix.append(int_list)
'''
del matrix[:]
matrix.append([131,673,234,103,18])
matrix.append([201,96,342,965,150])
matrix.append([630,803,746,422,111])
matrix.append([537,699,497,121,956])
matrix.append([805,732,524,37,331])
'''

def dijkstra(i,j):
	visited = set([])
	while True:
		if j == len(matrix)-1:
			return
		min =1000000000
		minIndex = (i,j)
		if i-1 >=0 and (i-1,j) not in visited:
			if matrix[i-1][j] + newMatrix[i][j] < newMatrix[i-1][j]:
				newMatrix[i-1][j] = matrix[i-1][j] + newMatrix[i][j]
		if j+1 < len(matrix) and (i,j+1) not in visited:
			if matrix[i][j+1] + newMatrix[i][j] < newMatrix[i][j+1]:
				newMatrix[i][j+1] = matrix[i][j+1] + newMatrix[i][j]
		if i+1 < len(matrix) and (i+1,j) not in visited:
			if matrix[i+1][j] + newMatrix[i][j] < newMatrix[i+1][j]:
				newMatrix[i+1][j] = matrix[i+1][j] + newMatrix[i][j]
		for l in xrange(0,len(matrix)):
			for k in xrange(0, len(matrix)):
				if newMatrix[l][k] < min and (l,k) not in visited:
					min = newMatrix[l][k]
					minIndex = (l,k)
		visited.add((i,j))
		i = minIndex[0]
		j = minIndex[1]
		
		
start = time.time()
minPath = 10000000
for i in xrange(0, len(matrix)):
	newMatrix = [[1000000 for x in xrange(0,len(matrix))] for x in xrange(0,len(matrix))]
	newMatrix[i][0] = 0
	dijkstra(i,0)
	for j in xrange(0,len(matrix)):
		if newMatrix[j][len(matrix)-1] + matrix[i][0] < minPath:
			minPath = newMatrix[j][len(matrix)-1]+ matrix[i][0]

end = time.time()
print minPath
print (end-start)*1000.0