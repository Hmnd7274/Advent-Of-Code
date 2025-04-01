#54870
#54897
#55260  WINNER
#55297
#55762
#58931

#54770
#54799
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

fichier = open("Day1/xavierB.txt", "r")
tableau = fichier.readlines()
#fichier = open("a.txt", "r")
#tableau = fichier.readlines()
calibrationValues = 0
a = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
import re
stp = 0
for element in tableau :
    print(element)
    numberI = 0
    firstNumberI = None
    lastNumberI = None
    firstNumber = None
    lastNumber = None
    element.strip()
    wordI = 0
    
    for letter in element :
        #print("letter =",letter)

        if letter.isdigit() and firstNumber == None:
            firstNumber = letter
            firstNumberI = numberI
            #print("firstnumber I =", firstNumberI)
            print("firstnumber =", firstNumber)

        if letter.isdigit() :
            lastNumber = letter
            lastNumberI = numberI
            #print("lastnumber I =", lastNumberI)
            print("lastnumber =", lastNumber)

        numberI += 1

        #print("firstnumber =",firstNumber)
        #print("lastnumber =",lastNumber)

    for i in range(len(a)) :
        print("a =", a[i])
        for z in range(len(re.findall(a[i], element))) :
            print("wordI + Z =", element.find(a[i]) + z)
            if element.find(a[i], element.find(a[i]) + z) != -1 :
                wordI = element.find(a[i])
                word = a[i]
                #print("wordI =", wordI, "word =", word)
                #print("gtdjviurhe =",wordI < firstNumberI)
                #print("vrdsvvezfvregrve =",wordI > lastNumberI)
                #print("LASTNUMBERIIIIIIIIII=", lastNumberI)

                if firstNumberI == None or wordI < firstNumberI :
                    firstNumber = transformator(word)
                    firstNumberI = wordI
                    #print("the first number =",firstNumber)

                if lastNumberI == None or wordI > lastNumberI :
                    lastNumber = transformator(word)
                    lastNumberI = wordI
                    #print("LAST NUMBER I", lastNumberI)
                    #print("the LAST number =",lastNumber)

        #if element.find(a[i]) != -1 :
        #    wordI = element.find(a[i])
        #    word = a[i]
            #print("wordI =", wordI, "word =", word)
            #print("gtdjviurhe =",wordI < firstNumberI)
            #print("vrdsvvezfvregrve =",wordI > lastNumberI)

            #if firstNumberI == None or wordI < firstNumberI :
            #    firstNumber = transformator(word)
            #    firstNumberI = wordI
                #print("the first number =",firstNumber)

            #if lastNumberI == None or wordI > lastNumberI :
            #    lastNumber = transformator(word)
            #    lastNumberI = wordI
                #print("LAST NUMBER I", lastNumberI)
                #print("the LAST number =",lastNumber)

            #if len(re.findall(a[i], element)) > 1 :
                #for b in range(len(re.findall(a[i], element))) :
                    #print(" WORD I =", wordI)

                    #x = element.replace(element[wordI], " ", 1)
                    #element = x.replace(element[wordI + 1], " ", 1)
                    #print("ELEMENT =", element)
                        
    print("firstnumber =",firstNumber)
    print("lastnumber =",lastNumber)

    print("a =", int(str(firstNumber) + str(lastNumber)))
    calibrationValues += int(str(firstNumber) + str(lastNumber))
    print(calibrationValues)
    stp += 1
print(stp)