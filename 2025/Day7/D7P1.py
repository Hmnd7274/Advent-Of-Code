file = open("ex.txt", "r")
puzzle = file.readlines()
lines = []
for l in puzzle :
    string = ""
    for i  in l :
        if i != "\n" :
            string += i
    lines.append(string)

def getSpeInd(line) :
    list = []
    for i in range(len(line)) :
        if line[i] == "^" :
            list.append(i)
    return list


laserIndexes = [lines[0].find("S")]
numberOfSplit = 0
for line in lines :
    seperatorIndexes = getSpeInd(line)

    newLaserIndexes = []
    for lI in laserIndexes :
        decouped = False
        for sepI in seperatorIndexes :
            if lI == sepI :
                if sepI - 1 not in newLaserIndexes :
                    newLaserIndexes.append(sepI-1)  
                if sepI + 1 not in newLaserIndexes :
                    newLaserIndexes.append(sepI+1)
                numberOfSplit += 1
                decouped = True
                break
        if not decouped :
            if lI not in newLaserIndexes :
                newLaserIndexes.append(lI)
    
    laserIndexes = [l for l in newLaserIndexes]
    newLaserIndexes.clear()

print(laserIndexes)
print(numberOfSplit)