fichier = open("calibrationDocument.txt", "r")
tableau = fichier.readlines()
calibrationValues = 0
for element in range(2) :
    print("elem =", tableau[element])
    b = tableau[element].replace(tableau[element][len(tableau[element]) - 1], "")
    element = b.replace(b[len(b) - 2], "")
    print("elem =", element)
    firstNumber = None
    lastNumber = None
    for letter in element :
        print("hehehehehe", letter)
        if not letter.islower() and firstNumber == None:
            firstNumber = letter
            print("firstNumber =", firstNumber)
        if not letter.islower() :
            print("letter1 = ", letter)
            lastNumber = letter
            print("lastNumber =", lastNumber)
            print("letter2 = ", letter)
        print("letter3 = ", letter)
    print("firstNumber =", firstNumber)
    print("lastNumber =", lastNumber)
    if lastNumber == None :
        lastNumber = firstNumber
    print("a =", firstNumber + lastNumber)
    calibrationValues += int(str(firstNumber) + str(lastNumber))
    print("calibrationvalues =",  calibrationValues)
print(calibrationValues)