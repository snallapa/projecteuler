def convertToRoman(number):
    roman = ""
    numerals = [(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (50, "L"), (90, "XC"), (100, "C"), (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")]
    while number > 0:
        for i in range(len(numerals) - 1, -1, -1):
            current = numerals[i]
            n = numerals[i-1]
            check = number // current[0]
            if check >= 1:
                roman += "".join([current[1] for i in range(check)])
                number -= check * current[0]
                break
    return roman

def romanToNumber(roman):
    number = 0
    romanToNumber = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    skip = False
    for i in range(len(roman)):
        if skip:
            skip = False
            continue
        if roman[i] == "I":
            if i < len(roman) - 1:
                if roman[i+1] == "V":
                    number += 4
                    skip = True
                    continue
                elif roman[i+1] == "X":
                    number += 9
                    skip = True
                    continue
            number += 1
        elif roman[i] == "X":
            if i < len(roman) - 1:
                if roman[i+1] == "L":
                    number += 40
                    skip = True
                    continue
                elif roman[i+1] == "C":
                    number += 90
                    skip = True
                    continue
            number += 10
        elif roman[i] == "C":
            if i < len(roman) - 1:
                if roman[i+1] == "D":
                    number += 400
                    skip = True
                    continue
                elif roman[i+1] == "M":
                    number += 900
                    skip = True
                    continue
            number += 100
        else:
            number += romanToNumber[roman[i]]
        
    return number

originalCharacters = 0
newCharacters = 0
with open("p089_roman.txt", "r") as f:
    for line in f:
        originalCharacters += len(line.strip())
        newCharacters += len(convertToRoman(romanToNumber(line.strip())))
print(originalCharacters)
print(newCharacters)
print(originalCharacters - newCharacters)
