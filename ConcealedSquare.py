n = 100000003
def checkSquare(num):
    if len(str(num)) != 17:
        return False
    digitsSplit = [int(i) for i in str(num)]
    counter = 1
    for i in range(0,18,2):
        if digitsSplit[i] != counter:
            return False
        counter = counter + 1
    return True

while True:
    square = n * n
    print(square)
    if checkSquare(square):
        print(square)
        break
    if n % 10 == 3:
        n = n + 4
    else:
        n = n + 6
