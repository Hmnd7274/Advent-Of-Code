with open("Advent Of Code 2022\Day 6\D6.txt", "r") as f:
    puzzleList = [line.strip() for line in f]
    puzzleString = puzzleList[0]
answer = 0
for inputIndex in range(len(puzzleString)-3) :
    if answer != 0 :
        break
    fourLString = puzzleString[inputIndex:inputIndex+4]
    counterOfDuplicatedLetter = 0
    # index = l'index de la lettre de la string de 4
    for index in range(len(fourLString)) :
        # si lettre présente en plusieurs fois
        if fourLString.count(fourLString[index]) > 1 :
            counterOfDuplicatedLetter += 1
            break
        if index == 3 and counterOfDuplicatedLetter == 0 and answer == 0:
            answer = inputIndex

realAnswer = inputIndex + 3
print(realAnswer)