Spiral = [[0 for x in range(0,1001)] for x in range(0,1001)]


def spiral():
	j = 500
	i = 500
	counter = 1
	directions = 1
	direction = 0
	while (j > 0 or i > 0 or j < 1000 or i < 1000):
		for k in range(0,2):
			for l in range(0,directions):
				if (i < 0 or j < 0 or j > 1000 or i > 1000):
					return;
				Spiral[i][j] = counter
				counter = counter + 1
				if direction == 0:
					i = i + 1
				if direction == 1:
					j = j + 1
				if direction == 2:
					i = i - 1
				if direction == 3:
					j = j - 1
			direction = direction + 1
			direction = direction % 4
		directions = directions + 1


spiral()
i =0
j=0
sum1 = 0
while i < 1001 or j < 1001:
	sum1 = sum1 + Spiral[i][j]
	i = i + 1
	j = j + 1

i = 1000
j = 0
while i < 1001 and j < 1001:
	sum1 = sum1 + Spiral[i][j]
	i = i - 1
	j = j + 1
sum1 = sum1 - Spiral[500][500]
print sum1
