# Euler 86
import math

def isSquare(num):
    root = math.sqrt(num)
    return int(root + 0.5) ** 2 == num

def integerShortestPath(a,b,c):
    return isSquare(a*a + (b+c)*(b+c))


count = 0
a = 0
while count < 1000000:
    a += 1
    for b in range(1, a+1):
        for c in range(1,b+1):
            if integerShortestPath(a,b,c):
                count += 1
    
# while count < 2000:
#     a += 1
#     for b in range(1,a):
#         if isSquare(a*a + b*b):
#             count += b//2
print(a)