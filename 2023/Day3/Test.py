with open("Day3/example.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

# def findNumber(ligne, index) :
#     print(ligne[index].isdigit())
#     if ligne[index].isdigit() :
#         nb = ligne[index]
#         a = 1
#         while a - 1 < index :
#             print("letter=", ligne[index - a])
#             if ligne[index - a].isdigit() :
#                 print(ligne[index - a])
#                 nb = str(ligne[index - a]) + nb
#                 print("nb=",nb)
#             a += 1
#         a = 1
#         print("longueur = ",len(ligne) - index)
#         while a < len(ligne) - index :
#             print("letter=", ligne[index + a],"a=", a)
#             if ligne[index + a].isdigit() :
#                 print(ligne[index + a])
#                 nb = nb + str(ligne[index + a])
#                 print("nb=",nb)
#             a += 1
        
#     return nb

# x = ".34567.....999..."
# print(findNumber(x, 5))

# a = [(1,2),(3,4)]
# b = (1,2)
# b = (2,b[1])
# c = ()
# c[0] = 2
# print(c)
# for x in range(1 + 1, 3) :
#     print(x)
# if 3 in [[3,2], [2,6]] :
#     print("gg")
def getIndexSymbol(line: str) :
    indexes = []
    i = 0
    for letter in line :
        if letter in operators :
            indexes.append(i)
        i += 1
    return indexes



def appendNumberToCountingN2(puzzleLineIndexFunc: int, indexOfMatch) :
    numberIndexRangeLine = numberIndexRangePuzzle[puzzleLineIndexFunc]
    indexOfNumberRangeInLine = 0
    for numberIndexRange in numberIndexRangeLine :
        number = 0
        if indexOfMatch in numberIndexRange and countingNumbers[puzzleLineIndexFunc][indexOfNumberRangeInLine] == []:
            for numberIndex in numberIndexRange :
                # print("number =", (puzzleList[puzzleLineIndexFunc][numberIndex]))
                number += int(puzzleList[puzzleLineIndexFunc][numberIndex])
            print("number =", (puzzleList[puzzleLineIndexFunc][numberIndex]))
            countingNumbers[puzzleLineIndexFunc][indexOfNumberRangeInLine].append(number)
        indexOfNumberRangeInLine += 1

operators = []
numberIndexRangePuzzle = []
symbolsIndexesPuzzle = []
number = []
countingNumbers = []
tab = []
numberTab = []

for line in puzzleList :
    print(line)
    # numberIndexRangePuzzle.append(getNumberRangeIndex(line))
    # symbolsIndexesPuzzle.append(getIndexSymbol(line))
    # for letter in line :
    #     if letter not in operators and not letter.isdigit():
    #         operators.append(letter)
# setNumberRangeIndexAndNumber(puzzleList)

print("tabIndex =")
for e in tab :
    print(e)
print("numberTab =")
for e in numberTab :
    print(e)

testTab = [1,"Y", "*"]
x = 2
if x == 3 :
    wyom = 1
if wyom or "*" in testTab :
    print("yeeeeeeee")