with open("Day3/example.txt", "r") as f:
    puzzleList = [line.strip() for line in f]


countingNumbers = []
operators = ["*"]

def getCircleCoordinate(symbolLineIndex, symbolLetterIndex) :
    if symbolLineIndex > 0 :
        aboveLine = puzzleList[symbolLineIndex - 1]
        for i in range(3) :
            if aboveLine[symbolLetterIndex - 1 + i].isdigit() :
                    

for lineIndex in range(len(puzzleList)) :
    line = puzzleList[lineIndex]
    for i in range(len(line)) :
        if line[i] == "*" :



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