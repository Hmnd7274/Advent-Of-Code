file = open("ex.txt", "r")
stringInput = file.readline()
puzzleLines = str.split(stringInput, ",")
# print(puzzleLines)

answ = []

for puzzleline in puzzleLines :
    leftRange = puzzleline[0:puzzleline.find("-")]
    rightRange = puzzleline[puzzleline.find("-")+1:]
    # print(leftRange, ";",rightRange)

    for number in range(int(leftRange), int(rightRange)+1) :
        for digitNumber in range(len(str(number))+1) :
            tempTab = []
            if len(str(number)) % (digitNumber+1) == 0 and len(str(number)) // (digitNumber+1) > 1 :
                # print(len(str(number)), ";", digitNumber+1)
                for patternsIndex in range(len(str(number)) // (digitNumber+1)) :

                    tempTab.append(str(number)[patternsIndex*(digitNumber+1):patternsIndex*(digitNumber+1)+digitNumber+1])
                # print("tab =", tempTab)
                bool = True
                for e in tempTab :
                    if e != tempTab[0]:
                        bool = False
                if bool and number not in answ:
                    answ.append(number)
x = 0
for e in answ :
    x += e
print(answ)
                    # "1234 1234"
print(x, "\n", 4174379265)