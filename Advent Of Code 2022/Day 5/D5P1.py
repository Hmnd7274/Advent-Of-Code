import copy
with open("Advent Of Code 2022\Day 5\D5.txt", "r") as f:
    inputCrates = []
    instructions = []
    for line in f :
        if line[0] == "m" :
            instructions.append(line.strip())
    f.close()
with open("Advent Of Code 2022\Day 5\D5.txt", "r") as f:
    for line in f :
        if len(line) == 1 :
            break
        inputCrates.append(line)
    f.close()

# Find how many columns
nbOfCrateColumns = str(inputCrates[len(inputCrates) -1]).replace(" ", "").strip()
nbCol = int(nbOfCrateColumns[len(nbOfCrateColumns)-1])

# Create the column list
stacks = []
for i in range(nbCol) :
    stacks.append(list())

for column in range(nbCol) :
    for line in range(len(inputCrates) - 1) :
        if (inputCrates[line][(column)*4 +1]) != " " :
            stacks[column].append(inputCrates[line][(column)*4 +1])

for stack in stacks :
    a = stack.reverse()
    stack = a

altStacks = copy.deepcopy(stacks)
for line in instructions :
    indexNb = 0
    nbToMoove = 0
    for i in range(len(line)) :
        if str(line[i]).isdigit() :
            indexNb = i
            nbToMoove = int(line[i])
            if str(line[i+1]).isdigit() :
                indexNb = i+1
                nbToMoove = int(str(nbToMoove) + str(line[i+1]))
                if str(line[i+2]).isdigit() :
                    indexNb = i+2
                    nbToMoove = int(str(nbToMoove) + str(line[i+2]))
            break
    fromStack = int(line[indexNb + 7])-1
    toStack = int(line[indexNb + 12])-1
    for i in range(nbToMoove) :
        crateToMoove = altStacks[fromStack][len(altStacks[fromStack])-1]
        altStacks[toStack].append(crateToMoove)
        altStacks[fromStack].pop(len(altStacks[fromStack])-1)

def showStacks(stacks) :
    list_len = [len(i) for i in stacks]
    showList = []
    for line in range(max(list_len)) :
        string = ""
        for column in range(9) :
            if line < len(stacks[column]) :
                letter = str(stacks[column][line])
                string += "["+letter+"] "
            else :
                string += "    "
        showList.append(string)
    showList.reverse()
    for st in showList :
        print(st)
showStacks(stacks)
print("\n")
showStacks(altStacks)

listFinal = [i[len(i)-1] for i in altStacks]
answer = ""
for i in listFinal :
    answer += i
print(answer)