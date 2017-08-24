import time
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

counter = 0
start = time.time()
for denom in range(4, 12001):
    lowerBound = int(denom / 3) + 1
    upperBound = int(denom / 2 + 0.5)
    for numer in range(lowerBound, upperBound):
        if gcd(numer, denom) == 1:
            counter = counter + 1
end = time.time()
print(counter)
print(str((end - start) * 1000) + "ms")
