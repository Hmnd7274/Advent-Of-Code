def transformator(word) :
    if word == "one" :
        return 1
    if word == "two" :
        return 2
    if word == "three" :
        return 3
    if word == "four" :
        return 4
    if word == "five" :
        return 5
    if word == "six" :
        return 6
    if word == "seven" :
        return 7
    if word == "eight" :
        return 8
    if word == "nine" :
        return 9

def findFirstNumber(line) :
    numberI = 0
    for letter in line :
        #print("letter =",letter)

        if letter.isdigit() and firstNumber == None:
            firstNumber = letter
            firstNumberI = numberI
            #print("firstnumber I =", firstNumberI)
            #print("firstnumber =", firstNumber)

        numberI += 1