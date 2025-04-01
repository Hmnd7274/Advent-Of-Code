#51
fichier = open("Day1/lastuser.txt", "r")
tableau = fichier.readlines()
calibrationValues = 0

for element in tableau :
    numberI = 0
    firstNumberI = 0
    lastNumberI = 0
    firstNumber = None
    lastNumber = None
#    print("element =", element)
    #b = element.replace(tableau[len(tableau) - 1], "")
    #element = b.replace(tableau[len(tableau) - 2], "")
    element.strip()
#    print("element =", element)

    for letter in element :
#        print("letter =", letter)
    
        if letter.isdigit() and firstNumber == None:
            firstNumber = letter
            firstNumberI = numberI

#            print("firstNumber =", firstNumber)
    
        if letter.isdigit() :
            lastNumber = letter
            lastNumberI = numberI
#            print("lastNumber =", lastNumber)
        
        numberI =+ 1
    
    print("a =", int(str(firstNumber) + str(lastNumber)))
    calibrationValues += int(str(firstNumber) + str(lastNumber))
    print(calibrationValues)