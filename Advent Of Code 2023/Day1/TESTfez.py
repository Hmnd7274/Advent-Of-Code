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

fichier = open("calibrationDocument.txt", "r")
tableau = fichier.readlines()
calibrationValues = 0
a = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

element = "ngfq4rsevenvngjtrjvvkcnvrs"
import re

numberI = 0
firstNumberI = None
lastNumberI = None
firstNumber = None
lastNumber = None
for letter in element :
    print("letter =",letter)
    if letter.isdigit() and firstNumber == None:
        firstNumber = letter
        firstNumberI = numberI
        print("firstnumber I =", firstNumberI)
        print("firstnumber =", firstNumber)
    if letter.isdigit() :
        lastNumber = letter
        lastNumberI = numberI
        print("lastnumber I =", lastNumberI)
        print("lastnumber =", lastNumber)
    numberI += 1
    print("firstnumber =",firstNumber)
    print("lastnumber =",lastNumber)
for i in range(len(a)) :
    if element.find(a[i]) >= 0 :
        wordI = element.find(a[i])
        word = a[i]
        #print("wordI =", wordI, "word =", word)
        #print("gtdjviurhe =",wordI < firstNumberI)
        #print("vrdsvvezfvregrve =",wordI > lastNumberI)
        if firstNumberI == None or wordI < firstNumberI :
            firstNumber = transformator(word)
            firstNumberI = wordI
            print("the first number =",firstNumber)
        if lastNumberI == None or wordI > lastNumberI :
            lastNumber = transformator(word)
            lastNumberI = wordI
            print("LAST NUMBER I", lastNumberI)
            print("the LAST number =",lastNumber)
        if len(re.findall(a[i], element)) > 1 :
            for b in range(len(re.findall(a[i], element))) :
                print("LA GROSSE COUILLE word I =", wordI)
                print("LA GROSSE COUILLE word I =", wordI)
                print("LA GROSSE COUILLE word I =", wordI)
                print("LA GROSSE COUILLE word I =", wordI)
                print("LA GROSSE COUILLE word I =", wordI)
                print("LA GROSSE COUILLE word I =", wordI)
                print("LA GROSSE COUILLE word I =", wordI)
                print("LA GROSSE COUILLE word I =", wordI)
                print("LA GROSSE COUILLE word I =", wordI)
                x = element.replace(element[wordI], " ", 1)
                element = x.replace(element[wordI + 1], " ", 1)
                print("ELEMENT =", element)
                if element.find(a[i]) >= 0 :
                    wordI = element.find(a[i])
                    word = a[i]
                    print("wordI =", wordI, "word =", word)
                    print("gtdjviurhe =",wordI < firstNumberI)
                    print("vrdsvvezfvregrve =",wordI > lastNumberI)
                    print("LASTNUMBERIIIIIIIIII=", lastNumberI)
                    if wordI < firstNumberI :
                        firstNumber = transformator(word)
                        firstNumberI = wordI
                        print("the first number =",firstNumber)
                    if wordI >= lastNumberI :
                        lastNumber = transformator(word)
                        lastNumberI = wordI
                        print("LAST NUMBER I", lastNumberI)
                        print("the LAST number =",lastNumber)
print("firstnumber =",firstNumber)
print("lastnumber =",lastNumber)
print("a =", int(str(firstNumber) + str(lastNumber)))
calibrationValues += int(str(firstNumber) + str(lastNumber))
print(calibrationValues)