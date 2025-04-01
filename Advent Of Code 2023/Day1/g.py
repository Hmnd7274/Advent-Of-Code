fichier = open("calibrationDocument.txt", "r")
tableau = fichier.readlines()
calibrationValues = 0
alp = [""]
firstNumber = None
lastNumber = None
tab = tableau[0].replace("/", "")
tab = tableau[0].replace("n", "")
print(tab)

for letter in tableau[0] :
    print(letter)

    if not letter.islower() and firstNumber == None:
        firstNumber = letter
        print("firstNumber =", firstNumber)
        lastNumber = letter

    elif not letter.islower() and letter == alp:
        print("letter" ,letter)
        lastNumber = letter
        print("lastNumber", lastNumber)

print("OOOOOOH", firstNumber)
print("AHHHHH", lastNumber)
print("a =", firstNumber + lastNumber)
calibrationValues += int(str(firstNumber) + str(lastNumber))
print("calibrationvalues =",  calibrationValues)
print("a = ")