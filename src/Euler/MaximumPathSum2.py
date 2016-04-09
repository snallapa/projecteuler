from copy import copy, deepcopy
import time
triangle = []
with open('triangle2.txt') as f:
    for line in f:
        int_list = [int(i) for i in line.split()]
        triangle.append(int_list)

dynamicTriangle = deepcopy(triangle)
for i in range(0, len(triangle)):
	for j in range(0, len(triangle[i])):
		if i ==0:
			continue
		if j == 0:
			dynamicTriangle[i][j] = dynamicTriangle[i][j] + dynamicTriangle[i-1][j]
		elif j == len(triangle[i]) - 1:
			dynamicTriangle[i][j] = dynamicTriangle[i][j] + dynamicTriangle[i-1][j-1]
		else:
			dynamicTriangle[i][j] = dynamicTriangle[i][j] + max(dynamicTriangle[i-1][j-1], dynamicTriangle[i-1][j])

max = 0
for n in dynamicTriangle[len(dynamicTriangle)-1]:
	if n > max:
		max = n
print max