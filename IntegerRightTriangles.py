import time
from fractions import gcd
start = time.time()
limit = 1500000
ppts = {}
for p in range(0, limit, 2):
    s = p/2
    sqS = int(s**0.5)
    sqtS = int((2 * s)**0.5) + 1
    if sqS % 2 == 0:
        sqS -= 1
    possible = 0
    for v in range(sqS, sqtS, 2):
        if s % v == 0:
            u = s/v
            if u < v and gcd(u, v) == 1:
                possible = possible + 1
    if possible == 1:
        ppts[p] = possible

answer = 0
pts = {}
for k, v in ppts.items():
    pts[k] = pts.get(k, 0) + 1
    s = 2
    while True:
        nxt = k * s
        if nxt > limit:
            break
        pts[nxt] = pts.get(nxt, 0) + 1
        s += 1
for k, v in pts.items():
    if v == 1:
        answer += 1
end = time.time()
print(answer)
print(str((end - start) * 1000) + "ms")

