with open("Advent Of Code 2022\Day 8\D8.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

def leftCalcVisiFrom(ligne, indexOfCTree, currTree) :
    ligneUntilI = ligne[:indexOfCTree]
    nbOfTrees = 0
    if len(ligneUntilI[::-1]) == 0 :
        return 0
    for index, tree in enumerate(ligneUntilI[::-1]) :
        if int(tree) < currTree :
            nbOfTrees += 1
        elif int(tree) >= currTree :
            nbOfTrees += 1
            return nbOfTrees
        if index == len(ligneUntilI[::-1])-1 :
            return nbOfTrees
        
def rightCalcVisiFrom(ligne, indexOfCTree, currTree) :
    ligneUntilI = ligne[indexOfCTree+1:]
    nbOfTrees = 0
    if len(ligneUntilI) == 0 :
        return 0
    for index, tree in enumerate(ligneUntilI) :
        if int(tree) < currTree :
            nbOfTrees += 1
        elif int(tree) >= currTree :
            nbOfTrees += 1
            return nbOfTrees
        if index == len(ligneUntilI)-1 :
            return nbOfTrees
        
def upCalcVisiFrom(colonne, indexOfCTree, currTree) :
    colUntilI = colonne[:indexOfCTree]
    nbOfTrees = 0
    if len(colUntilI[::-1]) == 0 :
        return 0
    for index, tree in enumerate(colUntilI[::-1]) :
        if int(tree) < currTree :
            nbOfTrees += 1
        elif int(tree) >= currTree :
            nbOfTrees += 1
            return nbOfTrees
        if index == len(colUntilI[::-1])-1 :
            return nbOfTrees
        
def downCalcVisiFrom(colonne, indexOfCTree, currTree) :
    colUntilI = colonne[indexOfCTree+1:]
    nbOfTrees = 0
    if len(colUntilI) == 0 :
        return 0
    for index, tree in enumerate(colUntilI) :
        if int(tree) < int(currTree) :
            nbOfTrees += 1
        elif int(tree) >= currTree :
            nbOfTrees += 1
            return nbOfTrees
        if index == len(colUntilI)-1 :
            return nbOfTrees
        
def calcScenicScore(currTree, indexOfLine, indexOfCol, line, col) :
    visFromLeft = (leftCalcVisiFrom(line, indexOfLine, currTree))
    visFromRight = (rightCalcVisiFrom(line, indexOfLine, currTree))

    visFromUp = (upCalcVisiFrom(col, indexOfCol, currTree))
    visFromDown = (downCalcVisiFrom(col, indexOfCol, currTree))
    return visFromLeft*visFromRight*visFromUp*visFromDown

colonnes = []
for oldOldI in range(len(puzzleList[0])) :
    colonnes.append("")

for oldLine in puzzleList :
    for oldI in range(len(oldLine)) :
        colonnes[oldI] += oldLine[oldI]

max = 0
for linesIndex, line in enumerate(puzzleList) :
    for lineI, tree in enumerate(line) :
        scenicScore = calcScenicScore(int(tree), lineI, linesIndex, line, colonnes[lineI])
        print(scenicScore)
        if scenicScore > max :
            max = scenicScore
print(max)