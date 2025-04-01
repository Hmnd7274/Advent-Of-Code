def transfm(word) :
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
cV = 0
a = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
import re

for element in tableau :
    firstN = None
    lastN = None
    firstNI = 0
    lastNI = 0
    lI = 0
    print("element =", element)

    for letter in element :

        if letter.isdigit() and firstN == None:
            firstN = letter
            firstNI = lI
        
        if letter.isdigit() :
            lastN = letter
            lastNI = lI
        
        lI += 1
    
    for i in range(len(a)) :
        
        if element.find(a[i]) == 1 :
            nb = transfm(a[i])
            nbI = element.find(a[i])

            if firstN == None or nbI < firstNI:
                firstN = nb
                firstNI = nbI
        
            if nbI > lastNI :
                lastN = nb
                lastNI = nbI
        
        elif element.find(a[i]) != -1 :
            
            for b in range(len(re.findall(a[i], element))) :
                nb = transfm(a[i])
                nbI = element.find(a[i], element.find(a[i]) + b)

                if firstN == None or nbI < firstNI:
                    firstN = nb
                    firstNI = nbI
        
                if nbI > lastNI :
                    lastN = nb
                    lastNI = nbI

    print("add =", int(str(firstN) + str(lastN)))
    cV += int(str(firstN) + str(lastN))
print(cV)