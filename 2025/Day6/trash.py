import re
file = open("ex.txt", "r")
puzzle = file.readlines()

puzzleTemp = []
# for l in puzzle :
#     lines.append(l.split(" "))

pattern = r'([.\S]+)'
for l in puzzle :
    puzzleTemp.append(re.findall(pattern, l))

columnes = []
for i in range(len(puzzleTemp[0])) :
    currCol = []
    for col in puzzleTemp :
        currCol.append(col[i])
    columnes.append(currCol)

print(columnes)


# recup symbol et length du nb le plus grand
col1 = columnes[0]
symbol = "*"
col1.remove("*")
print(col1)
length = 0
for nb in col1 :
    if len(nb) > length :
        length = len(nb)

def getSymbAndMaxLength(col) :
    symbol = ""
    for e in col :
        if not e.isdigit() :
            symbol = e
    maxLength = 0
    for nb in col :
        if len(nb) > maxLength :
            maxLength = len(nb)
    return symbol,maxLength


# ajuster la length des autres nb
for i in range(len(col1)) :
    if len(col1[i]) < length :
        col1[i] = "0"*(length - len(col1[i])) + col1[i]
print("col1",col1)

def adjustLength(col, maxLength) :
    for i in range(len(col)) :
        if len(col[i]) < maxLength :
            col[i] = "0"*(maxLength - len(col[i])) + col[i]


# changer d'axe de colonne
cephalopodsMadness = []
for nb in col1 :
    cephalopodsMadness.append("")
for nb in col1 :
    for i in range(len(nb)) :
        cephalopodsMadness[i] += str(nb)[i]

print("\ncepha",cephalopodsMadness)

# retirer les 0 qui cassent tout
listindex = 0
for nb in cephalopodsMadness :

    chelouindex = len(str(nb))-1

    while int(nb[chelouindex]) == 0 and chelouindex >= 0:

        cephalopodsMadness[listindex] = cephalopodsMadness[listindex][0:-1]
        chelouindex -= 1

    listindex += 1

print("cepha",cephalopodsMadness)


# faire operation en fonction de symbol
operation = 1
for nb in cephalopodsMadness :
    operation *= int(nb)

print(operation)

# for col in columnes :



# def mult(list) :
#     answer = 1
#     for l in list :
#         if l.isdigit() :
#             answer *= int(l)
#     return answer

# def add(list) :
#     answer = 0
#     for l in list :
#         if l.isdigit() :
#             answer += int(l)
#     return answer

# print(columnes)
# print(len(columnes))
# answer = 0
# for col in columnes :
#     symbol = col[-1]

#     if symbol == "*" :
#         answer += mult(col)

#     elif symbol == "+" :
#         answer += add(col)
    
# print(answer)