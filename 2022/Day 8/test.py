string = "54345"
string2 = string[:3]
string3 = string2[::-1]

def leftCalcVisiFrom(ligne, indexOfCTree, currTree) :
    ligneUntilI = ligne[:indexOfCTree]
    nbOfTrees = 0
    for index, tree in enumerate(ligneUntilI[::-1]) :
        if int(tree) < currTree :
            nbOfTrees += 1
        if int(tree) >= currTree :
            nbOfTrees += 1
            return nbOfTrees
        if index == len(ligneUntilI[::-1])-1 :
            return nbOfTrees
print(string[:3])
print(string[3+1:])