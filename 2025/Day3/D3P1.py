file = open("ex.txt", "r")
puzzleinput = file.readlines()

puzzlelines = []
for l in puzzleinput :
    newline = ""
    for s in l :
        if s.isdigit() :
            newline += s
    puzzlelines.append(newline)
print(puzzlelines)

answerTab = []

def getMax(str) :
    max1 = int(str[0])
    max1Index = 0
    i = 0
    for char in str :
        if int(char) > max1 :
            max1 = int(char)
            max1Index = i
        i += 1
    return max1, max1Index
print(getMax("1234"))

for line in puzzlelines :
    max1, max1Index = getMax(line)
    
    if max1Index == len(line)-1 :
        max1, max1Index = getMax(line[0:len(line)-1])

    newline = line[max1Index+1:]
    max2, max2Index = getMax(newline)

    print("max1 = ", max1, " ; max2 =", max2)
    print("newline = ", newline)
    answerTab.append(str(max1)+str(max2))

print(answerTab)
answer = 0
for e in answerTab :
    answer += int(e)
print(answer)