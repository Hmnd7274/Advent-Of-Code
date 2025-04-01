fichier = open("Day1/xavierB.txt", "r")
tableau = fichier.readlines()
cV = 0

for element in tableau :
    firstN = None
    lastN = None
    firstNI = None
    lastNI = None
    lI = 0
    print("element =", element)

    for letter in element :

        if letter.isdigit() and firstN == None:
            firstN = letter
            firstNI = lI
        
        if letter.isdigit() :
            lastN = letter
            lastNI = lI
        
        if letter == "o" and (len(element) -1) - lI >= 2 and element[lI + 1] == "n" and element[lI + 2] == "e" :
            if firstNI == None or lI < firstNI :
                firstN = 1
                firstNI = lI
            if lastNI == None or lI > lastNI :
                lastN = 1
                lastNI = lI
        
        if letter == "t" and (len(element) -1) - lI >= 2 and element[lI + 1] == "w" and element[lI + 2] == "o" :
            if firstNI == None or lI < firstNI :
                firstN = 2
                firstNI = lI
            if lastNI == None or lI > lastNI :
                lastN = 2
                lastNI = lI

        if letter == "t" and (len(element) -1) - lI >= 4 and element[lI + 1] == "h" and element[lI + 2] == "r" and element[lI + 3] == "e" and element[lI + 4] == "e" :
            if firstNI == None or lI < firstNI :
                firstN = 3
                firstNI = lI
            if lastNI == None or lI > lastNI :
                lastN = 3
                lastNI = lI

        if letter == "f" and (len(element) -1) - lI >= 3 and element[lI + 1] == "o" and element[lI + 2] == "u" and element[lI + 3] == "r" :
            if firstNI == None or lI < firstNI :
                firstN = 4
                firstNI = lI
            if lastNI == None or lI > lastNI :
                lastN = 4
                lastNI = lI

        if letter == "f" and (len(element) -1) - lI >= 3 and element[lI + 1] == "i" and element[lI + 2] == "v" and element[lI + 3] == "e" :
            if firstNI == None or lI < firstNI :
                firstN = 5
                firstNI = lI
            if lastNI == None or lI > lastNI :
                lastN = 5
                lastNI = lI        
        if letter == "s" and (len(element) -1) - lI >= 2 and element[lI + 1] == "i" and element[lI + 2] == "x" :
            if firstNI == None or lI < firstNI :
                firstN = 6
                firstNI = lI
            if lastNI == None or lI > lastNI :
                lastN = 6
                lastNI = lI

        if letter == "s" and (len(element) -1) - lI >= 4 and element[lI + 1] == "e" and element[lI + 2] == "v" and element[lI + 3] == "e" and element[lI + 4] == "n" :
            if firstNI == None or lI < firstNI :
                firstN = 7
                firstNI = lI
            if lastNI == None or lI > lastNI :
                lastN = 7
                lastNI = lI   

        if letter == "e" and (len(element) -1) - lI >= 4 and element[lI + 1] == "i" and element[lI + 2] == "g" and element[lI + 3] == "h" and element[lI + 4] == "t" :
            if firstNI == None or lI < firstNI :
                firstN = 8
                firstNI = lI
            if lastNI == None or lI > lastNI :
                lastN = 8
                lastNI = lI

        if letter == "n" and (len(element) -1) - lI >= 3 and element[lI + 1] == "i" and element[lI + 2] == "n" and element[lI + 3] == "e" :
            if firstNI == None or lI < firstNI :
                firstN = 9
                firstNI = lI
            if lastNI == None or lI > lastNI :
                lastN = 9
                lastNI = lI

        lI += 1
    print("add =", int(str(firstN) + str(lastN)))
    cV += int(str(firstN) + str(lastN))
print(cV)