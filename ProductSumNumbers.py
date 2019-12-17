# Euler 88
from math import log2
import time
def product(l):
    i = 1
    for k in l:
        i = i * k
    return i



def minK(k):
    if k == 2:
        return (4, [2,2])
    ones = k - 1 - int(log2(k) + 0.5)
    m = 100000
    ans = []
    while ones < k-1:
        real = k - ones
        nums = [2 for i in range(real)]
        place = 0
        while place < len(nums):
            s = sum(nums) + ones
            p = product(nums)
            if s == p and s < m:
                m = s
                ans = list(nums)
            if p > s:
                spot = 0
                found = False
                while spot < len(nums):
                    nums[spot] += 1
                    for i in range(spot):
                        nums[i] = nums[spot]
                    s = sum(nums) + ones
                    p = product(nums)
                    if p <= s:
                        found = True
                        break
                    spot += 1
                if not found:
                    break
                place = spot
            else:
                for i in range(len(nums)):
                    if nums[i] != k:
                        nums[i] += 1
                        break
                    else:
                        if nums[place] == k:
                            place += 1
                        if place == len(nums):
                            break
                        nums[i] = nums[place] + 1
        ones += 1
    return m, ans

# print(minK(1997))
ans = set([])
for i in range(2, 12001):
    val, _ = minK(i)
    ans.add(val)
    print(i)
print(sum(ans))
        
        
        

