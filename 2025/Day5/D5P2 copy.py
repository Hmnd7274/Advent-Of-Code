file = open("ex.txt", "r")
input = file.readlines()

puzzlelines = []
for l in input :
    if l.count("-") > 0 :
        string = l.split()[0]
        puzzlelines.append(string)
        # print(string)

rangesList = []
initRangeList = []
indexPuzzle = 0
while indexPuzzle < len(puzzlelines) and puzzlelines[indexPuzzle].count("-") > 0 :

    firstnb = puzzlelines[indexPuzzle][0:puzzlelines[indexPuzzle].find("-")]
    secondnb = puzzlelines[indexPuzzle][puzzlelines[indexPuzzle].find("-")+1:]

    rangesList.append((int(firstnb),int(secondnb)))
    initRangeList.append((int(firstnb),int(secondnb)))
  
    indexPuzzle += 1


tempList = []

def rmChevauchement(list : list, w) :
    tempList = []
    for i in range(w) :
        CURRENTLENGTH = len(list)
        boool = False
        tempList.clear()
        for e in list :
            tempList.append(e)
        trying = tempList == list
        while tempList == list :
            for min,max in list :
                for min2,max2 in list :

                    if min < min2 and min2 < max and max < max2 :
                        list.remove((min,max))
                        list.remove((min2,max2))
                        list.append((min,max2))
                        boool = True
                        break
                if boool :
                    break
            if not boool :
                print("WTF")
                break
        print(len(list))

def rmEntouré(list : list, w) :
    tempList = []
    for i in range(w) :
        CURRENTLENGTH = len(list)
        boool = False
        tempList.clear()
        for e in list :
            tempList.append(e)
        trying = tempList == list
        while tempList == list :
            for min,max in list :
                for min2,max2 in list :

                    if min < min2 and max2 < max :
                        list.remove((min,max))
                        list.remove((min2,max2))
                        list.append((min,max))
                        boool = True
                        break
                if boool :
                    break
            if not boool :
                print("WTF")
                break
        print(len(list))

def rmMinEgale(list : list, w) :
    tempList = []
    for i in range(w) :
        CURRENTLENGTH = len(list)
        boool = False
        tempList.clear()
        for e in list :
            tempList.append(e)
        trying = tempList == list
        while tempList == list :
            for min,max in list :
                for min2,max2 in list :

                    if min == min2 and max2 != max :
                        list.remove((min,max))
                        list.remove((min2,max2))
                        if max > max2 :
                            list.append((min,max))
                        if max2 > max :
                            list.append((min,max2))
                        boool = True
                        break
                if boool :
                    break
            if not boool :
                print("WTF")
                break
        print(len(list))

def rmMaxEgale(list : list, w) :
    tempList = []
    for i in range(w) :
        CURRENTLENGTH = len(list)
        boool = False
        tempList.clear()
        for e in list :
            tempList.append(e)
        trying = tempList == list
        while tempList == list :
            for min,max in list :
                for min2,max2 in list :

                    if min != min2 and max2 == max :
                        list.remove((min,max))
                        list.remove((min2,max2))
                        if min < min2 :
                            list.append((min,max))
                        if min2 < min :
                            list.append((min2,max))
                        boool = True
                        break
                if boool :
                    break
            if not boool :
                print("WTF")
                break
        print(len(list))


def rmMultiple(list : list, w) :
    tempList = []
    for i in range(w) :
        CURRENTLENGTH = len(list)
        boool = False
        tempList.clear()
        for e in list :
            tempList.append(e)
        trying = tempList == list
        while tempList == list :
            firstIndex = 0
            for min,max in list :
                if list.count((min,max)) > 1 :
                    list.remove((min,max))
                    boool = True
                    break
                if boool :
                    break
                firstIndex += 1
            if not boool :
                print("WTF")
                break
        print(len(list))

def rmMaxEgaleMin(list : list, w) :
    tempList = []
    for i in range(w) :
        CURRENTLENGTH = len(list)
        boool = False
        tempList.clear()
        for e in list :
            tempList.append(e)
        trying = tempList == list
        while tempList == list :
            for min,max in list :
                for min2,max2 in list :

                    if min == max2 and min2 != max :
                        list.remove((min,max))
                        list.remove((min2,max2))
                        list.append((min2,max))
                        boool = True
                        break
                if boool :
                    break
            if not boool :
                print("WTF")
                break
        print(len(list))

# rmChevauc rmEntouré rmMinEgale rmMaxEgale rmEgale
rmChevauchement(rangesList, 60)
rmEntouré(rangesList, 20)
rmMinEgale(rangesList, 20)
rmMaxEgale(rangesList, 20)
rmMultiple(rangesList, 20)
rmMaxEgaleMin(rangesList, 20)
# print(len(rangesList))

file12 = open("test.txt", "w")
for min,max in rangesList :
    file12.write(str(min)+"-"+str(max)+"\n")

answer = 0
for x,y in rangesList :
    answer += y - x + 1

print(answer)