import time

def number_list(number):
    return ''.join(str(x) for x in sorted([int(digit) for digit in str(number)]))

def findCubes(goal):
    number = 1
    cubes = {}
    while True:
        for key, value in cubes.items():
            if len(value) == goal:
                return min(value)
        cube = number**3
        digits = number_list(cube)
        if cubes.get(digits, None) == None:
            cubes[digits] = [cube]
        else:
            cubes[digits] = cubes[digits] + [cube]
        number = number + 1
start = time.time()
answer = findCubes(5)
end = time.time()
print(answer)
print(str((end - start) * 1000) + "ms")
