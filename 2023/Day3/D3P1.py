with open("Day3/example.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

# def getIndexSymbol(line: str) :
#     indexes = []
#     i = 0
#     for letter in line :
#         if letter in operators :
#             indexes.append(i)
#         i += 1
#     return indexes

# def getNumberRangeIndex(line: str) : # exclusif
#     tab = []
#     i = 0
#     for letter in line :
#         if i >= len(line) :
#             break
#         if line[i].isdigit() :
#             a = [i]
#             for x in range(i + 1, len(line)) :
#                 if not line[x].isdigit() or line[x] == line[-1] : # 012345 i = 1 ; x = i + 1 = 2
#                     break
#                 a.append(x)
#             tab.append(a)
#             i = x
#         i += 1
#     return tab

# def appendNumberToCountingN(line: str, indexOfMatch: int) :
#     letter = line[indexOfMatch]
#     i = 1
#     while letter[indexOfMatch + i] :
#         i += 1
#     lastNumero = line[indexOfMatch + i - 1]

# def appendNumberToCountingN2(puzzleLineIndexFunc: int, indexOfMatch) :
#     numberIndexRangeLine = numberIndexRangePuzzle[puzzleLineIndex]
#     indexOfNumberRangeInLine = 0
#     for numberIndexRange in numberIndexRangeLine :
#         number = 0
#         if indexOfMatch in numberIndexRange and countingNumbers[puzzleLineIndexFunc][indexOfNumberRangeInLine] == []:
#             for numberIndex in numberIndexRange :
#                 # print("number =", (puzzleList[puzzleLineIndexFunc][numberIndex]))
#                 number += int(puzzleList[puzzleLineIndexFunc][numberIndex])
#             print("number =", (puzzleList[puzzleLineIndexFunc][numberIndex]))
#             countingNumbers[puzzleLineIndexFunc][indexOfNumberRangeInLine].append(number)
#         indexOfNumberRangeInLine += 1

# def setNumberRangeIndexAndNumber(puzzleList: str) : # exclusif
#     for line in puzzleList :
#         indexTab = []
#         indexSymbolsTab = []
#         numbTab = []
#         emptyNumberTab = []
#         i = 0
#         for letter in line :
#             if i >= len(line) :
#                 break
#             if line[i].isdigit() :
#                 a = [i]
#                 numb = str(line[i])
#                 for letterIterator in range(i + 1, len(line)) :
#                     if not line[letterIterator].isdigit() or line[letterIterator] == line[-1] : # 012345 i = 1 ; letterIterator = i + 1 = 2
#                         break
#                     a.append(letterIterator)
#                     numb += line[letterIterator]
#                 emptyNumberTab.append([])
#                 indexTab.append(a)
#                 numbTab.append(numb)
#                 i = letterIterator
#             i += 1
#         for w in range(len(line)) :
#             if line[w] in operators :
#                 indexSymbolsTab.append(w)
        
#         numbersIndexesTab.append(indexTab)
#         symbolsIndexesTab.append(indexSymbolsTab)
#         numbersValueTab.append(numbTab)
#         countingNumbers.append(emptyNumberTab)

# operators = []

# numbersIndexesTab = []
# numbersValueTab = []
# symbolsIndexesTab = []
# countingNumbers = []
# victoryNumber = 0

# saves indexes of all operators
# saves indexes of all range of numbers
# INITIALISATION
# for line in puzzleList :
#     # print(line)
#     for letter in line :
#         if letter not in operators and not letter.isdigit() and letter != ".":
#             operators.append(letter)
# print(operators)
# setNumberRangeIndexAndNumber(puzzleList)

# for lineIndex in range(len(puzzleList)) :
#     numbersLineIndexes = numbersIndexesTab[lineIndex]
#     rangeIndex = 0
#     for numberIndexeRange in numbersLineIndexes :
#         for numberIndex in numberIndexeRange :
#             if numberIndex > 0 and numberIndex < len(line) - 1 and countingNumbers[lineIndex][rangeIndex] == [] :
                
#                 # check au dessus
#                 if lineIndex > 0 and countingNumbers[lineIndex][rangeIndex] == []:
#                     aboveChar = puzzleList[lineIndex - 1][numberIndex]
#                     leftAboveChar = puzzleList[lineIndex - 1][numberIndex - 1]
#                     rightAboveChar = puzzleList[lineIndex - 1][numberIndex + 1]
#                     aboveChars = [leftAboveChar, aboveChar, rightAboveChar]
#                     if any(ch in operators for ch in aboveChars) :
#                         countingNumbers[lineIndex][rangeIndex].append(numbersValueTab[lineIndex][rangeIndex])
                
#                 # check en dessous
#                 if lineIndex < len(puzzleList) - 1 and countingNumbers[lineIndex][rangeIndex] == []:
#                     underChar = puzzleList[lineIndex + 1][numberIndex]
#                     leftUnderChar = puzzleList[lineIndex + 1][numberIndex - 1]
#                     rightUnderChar = puzzleList[lineIndex + 1][numberIndex + 1]
#                     underChars = [leftUnderChar, underChar, rightUnderChar]
#                     if any(ch2 in operators for ch2 in underChars) :
#                         countingNumbers[lineIndex][rangeIndex].append(numbersValueTab[lineIndex][rangeIndex])
                
#                 # check à gauche
#                 if countingNumbers[lineIndex][rangeIndex] == []:
#                     leftChar = puzzleList[lineIndex][numberIndex - 1]
#                     if leftChar in operators :
#                         countingNumbers[lineIndex][rangeIndex].append(numbersValueTab[lineIndex][rangeIndex])

#                 # check à droite
#                 if countingNumbers[lineIndex][rangeIndex] == []:
#                     rightChar = puzzleList[lineIndex][numberIndex + 1]
#                     if rightChar in operators :
#                         countingNumbers[lineIndex][rangeIndex].append(numbersValueTab[lineIndex][rangeIndex])
#         rangeIndex += 1

def setSymbols() :
    for line in puzzleList :
        for letter in line :
            if letter != "." and not letter.isdigit() and letter not in operators :
                operators.append(letter) 

countingNumbers = []
operators = []

setSymbols()

for lineIndex in range(len(puzzleList)) :
    line = puzzleList[lineIndex]
    realCharIndex = 0
    for charIndex in range(len(puzzleList[lineIndex])) :
        if realCharIndex >= len(line) :
            break
        currentChar = puzzleList[lineIndex][realCharIndex]
        if currentChar.isdigit() :
            booleanNumbCounts = False
            number = ""
            for newCharIndex in range(charIndex, len(puzzleList[lineIndex])) : #..[12343]...
                if realCharIndex >= len(line) or not line[realCharIndex].isdigit() :
                    break
                
                number += str(line[realCharIndex])

                if not booleanNumbCounts :

                    # check au dessus
                    if lineIndex > 0 and realCharIndex > 0 and realCharIndex < len(line) - 1:

                        leftAboveChar = puzzleList[lineIndex - 1][realCharIndex - 1]
                        aboveChar = puzzleList[lineIndex - 1][realCharIndex]
                        rightAboveChar = puzzleList[lineIndex - 1][realCharIndex + 1]
                        aboveChars = [leftAboveChar, aboveChar, rightAboveChar]

                        if any(ch in operators for ch in aboveChars) :
                            booleanNumbCounts = True

                    # check en dessous
                    if lineIndex < len(puzzleList) - 1 and realCharIndex > 0 and realCharIndex < len(line) - 1 :

                        leftUnderChar = puzzleList[lineIndex + 1][realCharIndex - 1]
                        underChar = puzzleList[lineIndex + 1][realCharIndex]
                        rightUnderChar = puzzleList[lineIndex + 1][realCharIndex + 1]
                        underChars = [leftUnderChar, underChar, rightUnderChar]

                        if any(ch2 in operators for ch2 in underChars) :
                            booleanNumbCounts = True                           

                    # check à gauche
                    if realCharIndex > 0 :
                        leftChar = puzzleList[lineIndex][realCharIndex - 1]
                        if leftChar in operators :
                            booleanNumbCounts = True

                    # check à droite
                    if realCharIndex < len(line) - 1 :
                        rightChar = puzzleList[lineIndex][realCharIndex + 1]
                        if rightChar in operators :
                            booleanNumbCounts = True

                realCharIndex += 1
            if booleanNumbCounts :
                countingNumbers.append(number)
        realCharIndex += 1

print(countingNumbers)
victoryNumber = 0
for e in countingNumbers :
    victoryNumber += int(e)
print(victoryNumber)
# puzzleLineIndex = 0
# for lineIndex in range(len(puzzleList)) :
#     for symbolIndexes in symbolsIndexesTab[lineIndex] :
#             if puzzleLineIndex > 0 :
#                 for 
#             if # chercher les cases du dessous
# puzzleLineIndex = 0
# for numberIndexRangeLine in numberIndexRangePuzzle :
#     for numberIndexRange in numberIndexRangeLine :
#         for numberIndex in numberIndexRange :
#             if puzzleLineIndex > 0 : # si ligne 2
#                 if numberIndex > 0 : # si ch 2
#                 # puzzleLine = puzzleList[puzzleIndex - 1]
#                     symbolsIndexesLine = symbolsIndexesPuzzle[puzzleLineIndex - 1] # symbol de la ligne du dessus
#                     for symbolsIndex in symbolsIndexesLine :
#                             if (numberIndex - 1) == symbolsIndex > 0 : # check au-dessus ; si match : ajoute le nombres à counting numbers si pas déja fait
#                                 appendNumberToCountingN2(puzzleLineIndex, numberIndex)
#     puzzleLineIndex += 1


# print("\n Counting :")
# for e in countingNumbers :
#     for el in e :
#         for ele in el :
#             victoryNumber += int(ele)
#     # print(e)
# print("Victory =", victoryNumber)
# print("\n")
# for e in symbolsIndexesTab :
#     print(e)
# print("\n")
# for e in numbersIndexesTab :
#     print(e)
# print("\n")
# for e in numbersValueTab :
#     print(e)