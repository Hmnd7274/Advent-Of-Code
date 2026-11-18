file = open("ex.txt", "r")
puzzle = file.readlines()
lines = []

# retire les \n
for l in puzzle :
    string = ""
    for e in l :
        if e != "\n" :
            string += e
    lines.append(string)

# recupere l'input sous forme de colonnes
columns = []
for x in range(len(lines[0])) :
    list = []
    # print(x)

    for i in range(len(lines)) :
        # print(columns,"\n",list)
        list.append(lines[i][x])
    columns.append(list)

def indexListOfSpaces(list) :
    listIndex = []
    i = 0
    for l in list :
        null = True
        for char in l :
            if char != " " :
                null = False
                break
        if null :
            listIndex.append(i)
        i += 1
    return listIndex

betterList = []
i = 0
for index in indexListOfSpaces(columns) :
    betterList.append(columns[i:index])
    i = index + 1
betterList.append(columns[i:len(columns)])

for l in betterList :
    print(l)

def getSymbol(list) :
    for l in list :
        for x in l :
            if not x.isdigit() and x != " " :
                return x

goldenlist = []
for l in betterList :
    symbol = getSymbol(l)
    newOperation = [symbol]
    print(symbol)
    for nb in l :
        numberString = ""
        for i in range(len(nb)) :
            if nb[i].isdigit() :
                numberString += nb[i]
        if numberString != "" :
            newOperation.append(numberString)
    goldenlist.append(newOperation)

for l in goldenlist :
    print(l)

CEPHALOPODUS = 0
for ope in goldenlist :
    if ope[0] == "*" :
        answer = 1
        for i in range(1, len(ope)) :
            answer *= int(ope[i])
        CEPHALOPODUS += answer
        
    elif ope[0] == "+" :
        answer = 0
        for i in range(1, len(ope)) :
            answer += int(ope[i])
        CEPHALOPODUS += answer

print(CEPHALOPODUS)
# for operation in betterList :


# problems = [[]]
# for line in columns :
#     if all(map(lambda x: x == ' ', line)):
#         problems.append([])
#     else:
#         problems[-1].append(line)

# print("\nproblem",problems[0])
# betterList = columns.
    
# for col in columns :
#     sring = ""
#     for char in col :
#         if char.isdigit() :
#             string += char
#         listOfNumber.append(c)

# print(columns)
# print(lines)
# for l in columns :
#     print(l)