with open("Advent Of Code 2022\Day 8\D8.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

def leftCalcVisiFrom(ligne, indexOfCTree, currTree) :
    for index, tree in enumerate(ligne) :
        if index == indexOfCTree :
            return True
        if int(tree) >= int(currTree) :
            return False
        
def rightCalcVisiFrom(ligne, indexOfCTree, currTree) :
    for index, tree in enumerate(ligne[::-1]) :
        if index == len(ligne)-1 - indexOfCTree :
            return True
        if int(tree) >= int(currTree) :
            return False
        
def upCalcVisiFrom(colonne, indexOfCTree, currTree) :
    for index, tree in enumerate(colonne) :
        if index == indexOfCTree :
            return True
        if int(tree) >= int(currTree) :
            return False
        
def downCalcVisiFrom(colonne, indexOfCTree, currTree) :
    for index, tree in enumerate(colonne[::-1]) :
        if index == len(colonne)-1 - indexOfCTree :
            return True
        if int(tree) >= int(currTree) :
            return False
        
def checkForVisible(currTree, indexOfLine, indexOfCol, line, col) :
    visFromLeft = (leftCalcVisiFrom(line, indexOfLine, currTree))
    visFromRight = (rightCalcVisiFrom(line, indexOfLine, currTree))

    visFromUp = (upCalcVisiFrom(col, indexOfCol, currTree))
    visFromDown = (downCalcVisiFrom(col, indexOfCol, currTree))
    if visFromLeft or visFromRight or visFromUp or visFromDown :
        return True
    else :
        return False

colonnes = []
for oldOldI in range(len(puzzleList[0])) :
    colonnes.append("")

for oldLine in puzzleList :
    for oldI in range(len(oldLine)) :
        colonnes[oldI] += oldLine[oldI]

answer = len(colonnes[0])*2 + (len(puzzleList[0])-2)*2
string = ""

for linesIndex, line in enumerate(puzzleList) :
    if linesIndex == 0 or linesIndex == len(puzzleList)-1 :
        continue

    for lineI, tree in enumerate(line) :
        if lineI == 0 or lineI == len(line)-1 :
            continue
        if (checkForVisible(tree, lineI, linesIndex, line, colonnes[lineI])) :
            answer += 1
            string += "/visible"
        else :
            string += "/not"
print(answer)