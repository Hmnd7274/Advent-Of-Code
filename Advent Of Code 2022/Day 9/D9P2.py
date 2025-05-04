with open("Advent Of Code 2022\\Day 9\\D9.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

def tooClose(Hcoords, Tcoords) :
    Hlinepos = int(Hcoords[:Hcoords.find(";")])
    Hcolpos = int(Hcoords[Hcoords.find(";")+1:])
    Tlinepos = int(Tcoords[:Tcoords.find(";")])
    Tcolpos = int(Tcoords[Tcoords.find(";")+1:])

    dx = abs(Hlinepos - Tlinepos)
    dy = abs(Hcolpos - Tcolpos)
    if max(dx, dy) > 1 :
        return False
    return True

def calcEasySituation(Hlinepos, Hcolpos, Tlinepos, Tcolpos) :
    needTo = 0
    if Hlinepos == Tlinepos : # si même ligne
        if Hcolpos < Tcolpos :
            needTo = -1
        else :
            needTo = 1
    elif Hcolpos == Tcolpos : # si même colonne
        if Hlinepos < Tlinepos :
            needTo = -1
        else :
            needTo = 1
    return needTo
        
def calcNewCoords(Hcoords, Tcoords) :
    if not tooClose(Hcoords, Tcoords) :
        Hlinepos = int(Hcoords[:Hcoords.find(";")])
        Hcolpos = int(Hcoords[Hcoords.find(";")+1:])
        Tlinepos = int(Tcoords[:Tcoords.find(";")])
        Tcolpos = int(Tcoords[Tcoords.find(";")+1:])
        if Hlinepos == Tlinepos : # si même ligne
            if Hcolpos < Tcolpos :
                Tcolpos += -1
            else :
                Tcolpos += 1
        elif Hcolpos == Tcolpos : # si même colonne
            if Hlinepos < Tlinepos :
                Tlinepos += -1
            else :
                Tlinepos += 1
        else :
            if Hlinepos > Tlinepos and Hcolpos > Tcolpos : # H au dessus à droite
                Tlinepos += 1
                Tcolpos += 1
            elif Hlinepos > Tlinepos and Hcolpos < Tcolpos : # H au dessus à gauche
                Tlinepos += 1
                Tcolpos += -1
            if Hlinepos < Tlinepos and Hcolpos > Tcolpos : # H en dessous à droite
                Tlinepos += -1
                Tcolpos += 1
            elif Hlinepos < Tlinepos and Hcolpos < Tcolpos : # H en dessous à gauche
                Tlinepos += -1
                Tcolpos += -1
        return str(Tlinepos)+";"+str(Tcolpos)
    return Tcoords

ropeList = []
dictPos = ["0;0"]

for i in range(10) :
    ropeList.append("0;0")

for inputline in puzzleList :
    instruction = inputline[0]
    for i in range(int(inputline[2:])) :
        for indexRope, ropePart in enumerate(ropeList) :
            OldHcoords = ropePart
            OldTcoords = ropeList[indexRope+1]
            Hlinepos = int(OldHcoords[:OldHcoords.find(";")])
            Hcolpos = int(OldHcoords[OldHcoords.find(";")+1:])
            Tlinepos = int(OldTcoords[:OldTcoords.find(";")])
            Tcolpos = int(OldTcoords[OldTcoords.find(";")+1:])
            if indexRope == 0 :
                if instruction == "L" :
                    Hcolpos += -1
                elif instruction == "R" :
                    Hcolpos += +1
                elif instruction == "U" :
                    Hlinepos += +1
                elif instruction == "D" :
                    Hlinepos += -1
            newHcoords = str(Hlinepos)+";"+str(Hcolpos)
            newTcoords = calcNewCoords(newHcoords, OldTcoords)
            ropeList[indexRope] = newHcoords
            ropeList[indexRope+1] = newTcoords
            if indexRope == len(ropeList)-2 :
                if not (newTcoords in dictPos) :
                    dictPos.append(newTcoords)
                break
print(len(dictPos))