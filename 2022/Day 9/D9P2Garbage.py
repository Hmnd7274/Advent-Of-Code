with open("Advent Of Code 2022\Day 9\D9.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

listPos = ["0;0"]
rope = []

for i in range(10) :
    rope.append("0;0")
print(rope)
w = 0
for line in puzzleList :
    instruction = line[0]
    for i in range(int(line[2:])) :
        for indexRope, ropePart in enumerate(rope) :
            w +=1
            if indexRope == len(rope)-1 :
                break
            HcolPos = int(ropePart[:ropePart.find(";")])
            HlinePos = int(ropePart[ropePart.find(";")+1:])

            TcolPos = int(rope[indexRope+1][:rope[indexRope+1].find(";")])
            TlinePos = int(rope[indexRope+1][rope[indexRope+1].find(";")+1:])
            if indexRope == 0 :
                if instruction == "L" :
                    HcolPos += -1
                elif instruction == "R" :
                    HcolPos += +1
                elif instruction == "U" :
                    HlinePos += +1
                elif instruction == "D" :
                    HlinePos += -1

            #                                                HHH                      ...                                                ...                                                  ...                                                .H.                                              ...                                                  ...                                                  H..                                                  ..H
            #                     H covers T              or HTH -->                  HT.                                                .TH                                                  .T.                                                .T.                                              .T.                                                  .T.                                                  .T.                                                  .T.
            #                                                HHH                      ...                                                ...                                                  .H.                                                ...                                              H..                                                  ..H                                                  ...                                                  ...
            if (HcolPos == TcolPos and HlinePos == TlinePos) or (HcolPos == TcolPos-1 and HlinePos == TlinePos) or (HcolPos == TcolPos+1 and HlinePos == TlinePos) or (HlinePos == TlinePos-1 and HcolPos == TcolPos) or (HlinePos == TlinePos+1 and HcolPos == TcolPos) or (HcolPos == TcolPos-1 and HlinePos == TlinePos-1) or (HcolPos == TcolPos+1 and HlinePos == TlinePos-1) or (HcolPos == TcolPos-1 and HlinePos == TlinePos+1) or (HcolPos == TcolPos+1 and HlinePos == TlinePos+1):
                HPosSTR = str(HcolPos) + ";" + str(HlinePos)
                TPosSTR = str(TcolPos) + ";" + str(TlinePos)

                rope[indexRope] = HPosSTR
                rope[indexRope+1] = TPosSTR
                continue
            #               .....
            #               H.T.H
            #               .....
            elif (HcolPos == TcolPos-2 and HlinePos == TlinePos) :
                TcolPos += -1
            elif (HcolPos == TcolPos+2 and HlinePos == TlinePos) :
                TcolPos += 1
            #               ..H..
            #               .....
            #               ..T..
            #               .....
            #               ..H..
            elif (HcolPos == TcolPos and HlinePos == TlinePos-2) :
                TlinePos += -1
            elif (HcolPos == TcolPos and HlinePos == TlinePos+2) :
                TlinePos += 1
            #               .H.H.
            #               H...H
            #               ..T..
            #               H...H
            #               .H.H.
            elif (HcolPos == TcolPos-1 and HlinePos == TlinePos-2) or (HcolPos == TcolPos-2 and HlinePos == TlinePos-1):
                TcolPos += -1
                TlinePos += -1
            elif (HcolPos == TcolPos-1 and HlinePos == TlinePos+2) or (HcolPos == TcolPos-2 and HlinePos == TlinePos+1) :
                TcolPos += -1
                TlinePos += +1
            elif (HcolPos == TcolPos+1 and HlinePos == TlinePos-2) or (HcolPos == TcolPos+2 and HlinePos == TlinePos-1) :
                TcolPos += +1
                TlinePos += -1
            elif (HcolPos == TcolPos+1 and HlinePos == TlinePos+2) or (HcolPos == TcolPos+2 and HlinePos == TlinePos+1) :
                TcolPos += +1
                TlinePos += +1

            HPosSTR = str(HcolPos) + ";" + str(HlinePos)
            TPosSTR = str(TcolPos) + ";" + str(TlinePos)
            print(TPosSTR)
            if indexRope == len(rope)-2 and (not TPosSTR in listPos) :
                listPos.append(TPosSTR)
            
            rope[indexRope] = HPosSTR
            rope[indexRope+1] = TPosSTR

            
print(rope)
print("listpos =",listPos)
print("answer =", len(listPos), "w=", w)

# print(listPos)
# showLine = []
# maxL = int(0)
# maxC = int(0)
# for coords in listPos :
#     if int(coords[:coords.find(";")]) >= int(maxL) :
#         maxL = int(coords[:coords.find(";")])+10000
#     if int(coords[coords.find(";")+1:]) >= int(maxC) :
#         maxC = int(coords[coords.find(";")+1:])+1000
# # print(maxL, maxC)
# for i in range(maxL) :
#     showLine.append([])
# for x in range(len(showLine)) :
#     for i in range(maxC) :
#         showLine[x].append(".")
# for coords in listPos :
#     a = int(coords[:coords.find(";")])
#     b = int(coords[coords.find(";")+1:])
#     showLine[a][b] = "#"
#     if (a == 0 and b == 0) :
#         showLine[a][b] = "S"
# # for l in showLine :
# #     print(l)
# showLine.reverse()
# # print("\n")
# for l in showLine :
#     string = ""
#     for l2 in l :
#         string += l2
#     # print(string)