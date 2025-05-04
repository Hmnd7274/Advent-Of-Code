with open("Advent Of Code 2022\Day 6\D6.txt", "r") as f:
    puzzleList = [line.strip() for line in f]
    puzzleString = puzzleList[0]
answer = 0
for inputIndex in range(len(puzzleString)-13) :
    if answer != 0 :
        break
    fourteenLString = puzzleString[inputIndex:inputIndex+14]
    counter = 0
    # index = l'index de la lettre de la string de 14
    for index in range(len(fourteenLString)) :
        # si lettre présente en plusieurs fois
        if fourteenLString.count(fourteenLString[index]) > 1 :
            counter += 1
            break
        if index == 13 and counter == 0 and answer == 0:
            answer = inputIndex

realAnswer = inputIndex + 13
print(realAnswer)