max = 10
for x in range(max) :
    if x == 0 :
        listA = ["1"]
        listB = ["1"]
        print(listB)

    else :
        listA = listB.copy()

        for i in range(len(listA)) :
            if i == 0 :
                listB[i] = "1"
            if i > 0 :
                listB[i] = str(int(listA[i - 1]) + int(listA[i]))
            if len(listA) == len(listB) :
                listB.append("1")
    spaces = ""
    for z in range(max - x) :
        spaces += " "
    print(x, "therme :", spaces, listB)