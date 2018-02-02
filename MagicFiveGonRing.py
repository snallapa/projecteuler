from itertools import permutations

numbers = [i for i in range(1,11)]

iterations = list(permutations(numbers, 3))
iterationsSummed = list(map(sum, iterations))
counter = 0
sumDict = {}
for iteration in iterationsSummed:
    sumDict[iteration] = sumDict.get(iteration, []) + [iterations[counter]]
    counter = counter + 1

def checkNumericalLowest(values):
    value = values[0]
    for check in values[1:]:
        if check[0] < value[0]:
            return False
    return True

answerDict = {}
for key, values in sumDict.items():
    for value in values:
        finalAnswer = [value]
        currentPossibilities = sumDict[key]
        sharedElement = value[2]
        nextPossibilities = list(filter((lambda x: x[1] == sharedElement), currentPossibilities))
        for possibility in nextPossibilities:
            secondPossibilities = list(filter((lambda x: x[1] == possibility[2]), currentPossibilities))
            for secondPossibility in secondPossibilities:
                thirdPossibilities = list(filter((lambda x: x[1] == secondPossibility[2]), currentPossibilities))
                for thirdPossibility in thirdPossibilities:
                    #final step
                    lastSharedElement = value[1]
                    newSharedElement = thirdPossibility[2]
                    finalPossibilities = list(filter((lambda x: x[2] == lastSharedElement and x[1] == newSharedElement), currentPossibilities))
                    if len(finalPossibilities) != 0:
                        for final in finalPossibilities:
                            finalAnswer = [value, possibility, secondPossibility, thirdPossibility, final]
                            check = list(set([i for sub in finalAnswer for i in sub]))
                            if len(check) == len(numbers) and checkNumericalLowest(finalAnswer):
                                answerDict[key] = answerDict.get(key, []) + [(value, possibility, secondPossibility, thirdPossibility, final)]
print(answerDict)
def combine(answer):
    flattened = [i for sub in answer for i in sub]
    return int("".join([str(i) for i in flattened]))

answers = []
for key, values in answerDict.items():
    intValues = list(map(combine, values))
    for value in intValues:
        answers.append(value)

print(max(list(filter((lambda x: len(str(x)) == 16), answers))))
