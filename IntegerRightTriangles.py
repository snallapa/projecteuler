def is_square(n):
    return n**0.5 == int(n**0.5)
answer = 0
for p in range(1500000):
    count = 0
    for h in range(p):
         a = 2
         b = -2 * (p - h)
         c = p * p - 2 * p * h
         desc = b*b - 4 * a * c
         leg1 = (-b + desc**0.5)/(2 * a)
         leg2 = (-b - desc**0.5)/(2 * a)
         if desc >=0 and is_square(desc) and leg1 > 0 and leg2 > 0:
             count = count + 1
    if count == 1:
        answer = answer + 1

print(answer)        
