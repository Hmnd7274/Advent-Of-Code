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
print(nbOfCrateColumns)
nbCol = int(nbOfCrateColumns[len(nbOfCrateColumns)-1])
print(nbCol)

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

listg = [3,5,8]
listg.pop(len(listg)-1)
print(listg)
listg.append(4)
print(listg)