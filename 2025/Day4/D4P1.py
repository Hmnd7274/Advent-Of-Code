file = open("ex.txt", "r")
puzzleinput = file.readlines()

puzzlelines = []
for l in puzzleinput :
    string = l.split()[0]
    puzzlelines.append(string)
    print(string, len(string))

relatPos = [(-1, -1),(-1, 0),(-1, 1)
            ,(0, -1),(0, 1),
            (1, -1),(1, 0),(1, 1)]

def lessThan4(x, y) :
    numberOfPQ = 0
    for a,b in relatPos :
        newXPos = x + a
        newYPos = y + b
        if (newXPos >= 0 and newXPos < len(puzzlelines[0])) and (newYPos >= 0 and newYPos < len(puzzlelines)) :
            if puzzlelines[newXPos][newYPos] == "@" :
                numberOfPQ += 1
    if numberOfPQ >= 4 :
        return False
    else :
        # print("En voila un : ", x, ";",y)
        return True

PQAccessible = 0
for x in range(len(puzzlelines)) :
    for y in range(len(puzzlelines[0])) :
        # if x == 4 and y == 9 :
        #     print("WTF")
        if puzzlelines[x][y] == "@" :
            if lessThan4(x, y) :
                PQAccessible += 1

print(PQAccessible)