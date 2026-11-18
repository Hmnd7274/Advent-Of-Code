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

def mult(list) :
    answer = 1
    for l in list :
        if l.isdigit() :
            answer *= int(l)
    return answer

def add(list) :
    answer = 0
    for l in list :
        if l.isdigit() :
            answer += int(l)
    return answer

print(columnes)
print(len(columnes))
answer = 0
for col in columnes :
    symbol = col[-1]

    if symbol == "*" :
        answer += mult(col)

    elif symbol == "+" :
        answer += add(col)
    
print(answer)