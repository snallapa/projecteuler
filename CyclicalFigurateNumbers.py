import time
def triangularList(lowerbound, upperBound):
    numbers = [1]
    n = 2
    while numbers[len(numbers) - 1] < upperBound:
        numbers.append(int(n * (n + 1) / 2))
        n = n + 1
    return list(filter((lambda x: x > lowerbound and x < upperBound), numbers))

def squareList(lowerbound, upperBound):
    numbers = [1]
    n = 2
    while numbers[len(numbers) - 1] < upperBound:
        numbers.append(int(n * n))
        n = n + 1
    return list(filter((lambda x: x > lowerbound and x < upperBound), numbers))

def pentagonalList(lowerbound, upperBound):
    numbers = [1]
    n = 2
    while numbers[len(numbers) - 1] < upperBound:
        numbers.append(int(n * (3*n-1) /2))
        n = n + 1
    return list(filter((lambda x: x > lowerbound and x < upperBound), numbers))

def hexagonalList(lowerbound, upperBound):
    numbers = [1]
    n = 2
    while numbers[len(numbers) - 1] < upperBound:
        numbers.append(int(n * (2*n-1)))
        n = n + 1
    return list(filter((lambda x: x > lowerbound and x < upperBound), numbers))

def heptagonalList(lowerbound, upperBound):
    numbers = [1]
    n = 2
    while numbers[len(numbers) - 1] < upperBound:
        numbers.append(int(n * (5*n-3)/2))
        n = n + 1
    return list(filter((lambda x: x > lowerbound and x < upperBound), numbers))

def octagonalList(lowerbound, upperBound):
    numbers = [1]
    n = 2
    while numbers[len(numbers) - 1] < upperBound:
        numbers.append(int(n * (3*n - 2)))
        n = n + 1
    return list(filter((lambda x: x > lowerbound and x < upperBound), numbers))

def isCyclic(numbers):
    return sorted([int(str(x)[2:])] for x in numbers) == sorted([int(str(x)[:2])] for x in numbers)

triangle = triangularList(1000, 10000)
square = squareList(1000, 10000)
pentagonal = pentagonalList(1000, 10000)
hexagonal = hexagonalList(1000, 10000)
heptagonal = heptagonalList(1000, 10000)

def findCycle(tuple):
    cycle = tuple[0]
    listsToCheck = tuple[1]
    if len(listsToCheck) == 0:
        return [(cycle, [])]
    cyclePossibilities = []
    for listCheck in listsToCheck:
        first2 = [int(str(x)[:2]) for x in listCheck]
        if int(str(cycle[len(cycle) - 1])[2:]) in first2:
            newCycleNumber = listCheck[first2.index(int(str(cycle[len(cycle) - 1])[2:]))]
            newListsToCheck = list(listsToCheck)
            newListsToCheck.remove(listCheck)
            cyclePossibilities.append((cycle + [newCycleNumber], newListsToCheck))

    return cyclePossibilities


octagonal = octagonalList(1000, 10000)
start = time.time()
for number1 in octagonal:
    listsCheck = [triangle, square, pentagonal, hexagonal, heptagonal]
    possibilities = findCycle(([number1], listsCheck))
    for i in range(6):
        if len(possibilities) == 0:
            break
        newPossibilities = []
        for possibility in possibilities:
            newPossibilities = newPossibilities + findCycle(possibility)
        possibilities = newPossibilities
    cycles = [cycle[0] for cycle in possibilities]
    found = False
    for cycle in cycles:
        if isCyclic(cycle):
            print(sum(cycle))
            found = True
    if found:
        break
end = time.time()
print(str((end - start) * 1000) + "ms")
