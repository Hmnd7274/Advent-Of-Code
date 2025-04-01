#tab = ["ghhj", "ktbh"]
#print(tab[0][1])
#calibrationValues = ""
#calibrationValues += str(0) + str(5)
#print(calibrationValues)
fichier = open("calibrationDocument.txt", "r")
tableau = fichier.readlines()
calibrationValues = 0
tab = ["anj1oikjjh6", "40", "jkcejhsio6vrjkrn0"]
tabl = ["1"]
for i in range(1) :
    firstNumber = None
    lastNumber = None
    for letter in tabl[i] :
#        print("letter =", letter)
        if not letter.islower() and firstNumber == None:
            firstNumber = letter
        elif not letter.islower() :
            lastNumber = letter
#        print(firstNumber, lastNumber)
#    print("add", int(str(firstNumber) + str(lastNumber)))
    if lastNumber == None :
        lastNumber = firstNumber
    calibrationValues += int(str(firstNumber) + str(lastNumber))
#    print("i =", i)
print("a =", calibrationValues)