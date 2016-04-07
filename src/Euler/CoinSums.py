change = [0,1,2,5,10,20,50,100,200]
totalChange = [[0 for x in range(0,201)] for x in range(0,len(change))]
totalChange[0][0] = 1
def numberChange():
	for i in range(len(change)):
		for j in range(len(totalChange[0])):
			if j == 0:
				totalChange[i][j] = 1
			if change[i] <= j:
				totalChange[i][j] = totalChange[i-1][j] + totalChange[i][j-change[i]]
			else:
				totalChange[i][j] = totalChange[i-1][j]


numberChange()
print totalChange[8][200]