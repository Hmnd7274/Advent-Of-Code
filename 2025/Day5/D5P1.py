file = open("ex.txt", "r")
input = file.readlines()

puzzlelines = []
for l in input :
    if len(l.split()) > 0 :
        string = l.split()[0]
        puzzlelines.append(string)
        # print(string)

rangesList = []
indexPuzzle = 0
while puzzlelines[indexPuzzle].count("-") > 0 :

    firstnb = puzzlelines[indexPuzzle][0:puzzlelines[indexPuzzle].find("-")]
    secondnb = puzzlelines[indexPuzzle][puzzlelines[indexPuzzle].find("-")+1:]

    rangesList.append((int(firstnb),int(secondnb)))
  
    indexPuzzle += 1

print(rangesList)

nbOfFresh = 0
for i in range(indexPuzzle, len(puzzlelines)) :

    for min, max in rangesList :

        if min <= int(puzzlelines[i]) <= max :
            nbOfFresh += 1
            print("fresh ingredient = ",puzzlelines[i])
            break

print(nbOfFresh)