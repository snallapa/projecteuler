import math
numberList = []
with open('base_exp.txt') as f:
    for line in f:
        int_list = [int(i) for i in line.split(",")]
        numberList.append(int_list)

max = 0.0
maxIndex = 0
for i in xrange(0,len(numberList)):
	num = numberList[i]
	exponent = num[1]*math.log(num[0])
	if exponent > max:
		max = exponent
		maxIndex = i+1
print maxIndex