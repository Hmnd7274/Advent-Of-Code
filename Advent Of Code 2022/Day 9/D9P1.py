with open("Advent Of Code 2022\\Day 9\\D9.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

HlinePos = 0
HcolPos = 0
TlinePos = 0
TcolPos = 0
listPos = ["0;0"]

for line in puzzleList :
    instruction = line[0]
    for i in range(int(line[2:])) :
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
        
        if not ((str(TlinePos) + ";" + str(TcolPos)) in listPos) :
            listPos.append((str(TlinePos) + ";" + str(TcolPos)))
print(len(listPos))