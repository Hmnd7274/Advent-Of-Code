file = open("ex.txt", "r")
puzzleinput = file.readlines()

puzzlelines = []
for l in puzzleinput :
    newline = ""
    for s in l :
        if s.isdigit() :
            newline += s
    puzzlelines.append(newline)
print("PUZZLLEEE =", puzzlelines, "\n")

answerTab = []

def getMaxWith11(str) :
    lineToSearch = str[0:len(str)-11]
    max1 = int(lineToSearch[0])
    max1Index = 0
    i = 0
    for char in lineToSearch :
        if int(char) > max1 :
            max1 = int(char)
            max1Index = i
        i += 1
    return max1, max1Index

def getMaxWithI(str, i) :
    lineToSearch = str[0:len(str)-i]
    max1 = int(lineToSearch[0])
    max1Index = 0
    i = 0
    for char in lineToSearch :
        if int(char) > max1 :
            max1 = int(char)
            max1Index = i
        i += 1
    return max1, max1Index


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

for line in puzzlelines :
    index = 0
    myline = line
    nb = ""
    
    for i in range(11, -1, -1) :
        lineToSearch = myline[0:len(myline)-i]
        max, index = getMaxWithI(myline, i)
        nb += str(max)
        myline = myline[index+1:]
    answerTab.append(nb)

print(answerTab)
answer = 0
for e in answerTab :
    answer += int(e)
print(answer)
print(3121910778619)