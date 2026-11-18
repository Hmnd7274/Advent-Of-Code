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

# print(rangesList)

# freshList = []
betterlist = []
for l,k in rangesList :
    betterlist.append((l,k))

# for i in range(len(rangesList)) :
#     if rangesList[i] != betterlist[i] :
#         print("WTFFF")
#         break
# print(betterlist, "\n")
# supprimed = 0
# ajouted = 0
print("eheh", len(rangesList))
for i in range(100) :
    booool = False
    for x in range(len(rangesList)) :
        min,max = rangesList[i]
        x = 0
        for min2, max2 in rangesList :
            if x != 0 :
                if min < min2 < max and max < max2 :
                    # print(("eheh : ", min,max, " 2 :", min2,max2))
                    bool1 = (min, max) in betterlist
                    bool2 = (min2, max2) in betterlist
                    if (min, max) in betterlist :
                        betterlist.remove((min, max))
                        # print("minmax removed")
                        # supprimed += 1
                    if (min2, max2) in betterlist :
                        betterlist.remove((min2, max2))
                        # print("2 removed")
                        # supprimed += 1
                    if (min, max2) not in betterlist :
                        betterlist.append((min, max2))
                        # print("ajouted")
                        # ajouted += 1
                        rangesList.clear()
                        for e in betterlist :
                            rangesList.append(e)
                            booool = True
                        break
            x += 1
        if booool :
            break
                    # if len(rangesList) < len(betterlist) :
                        # print(("c'est louche"))
                    # print("lenBetterlist === ",len(betterlist))


    # betterlist.clear()
    # for e in rangesList :
    #     betterlist.append(e)    

print()

print(len(initRangeList))
print(len(betterlist))

# for e in betterlist :
#     if betterlist.count(e) > 1 :
#         betterlist.remove(e)

#     rangesList.clear()
#     for l in betterlist :
#         rangesList.append(l)

# goldenlist = []
# for e in betterlist :
#     goldenlist.append(e)

# mainIndex = 0
# for x,l in betterlist :
#     whereisit = 0
#     for w,k in betterlist :
#         a = 3
#         b=12
#         if x < w < l and l < k :
#             print("MAININDEX =", mainIndex, ";", whereisit,"\n")
#             print("bizarre")
#             print(x, ";", l)
#             print(w, ";", k)
#             if (x,l) not in goldenlist and (w,k) not in goldenlist :
#                 print("CCHELOU")
#                 break
#             if (x,l) in goldenlist :
#                 goldenlist.remove((x,l))
#             if (w,k) in goldenlist :
#                 goldenlist.remove((w,k))
#             goldenlist.append((x,k))
#             break
#         whereisit += 1
#     mainIndex += 1
        

# print("supprimé",supprimed)
# print("ajouter :",ajouted)

# print(len(goldenlist))

# filewrite = open("test.txt", "w")
# for l in betterlist :
#     filewrite.write(str(l[0])+"-"+str(l[1])+"\n")

# filewrite = open("test2.txt", "w")
# for l in betterlist :
#     filewrite.write(str(l[0])+"-"+str(l[1])+"\n")

# answer = 0
# for x,y in betterlist :
#     answer += y - x + 1

# print(answer)