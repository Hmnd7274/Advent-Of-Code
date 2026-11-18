import random
import math
# print("UW19"[2:])
# print("UW19"[:2])
# coords = "1;2"
# print(coords[:coords.find(";")])

# puzzleList = ["R 10"]
# rope = []

# for i in range(2) :
#     rope.append("0;0")
# print(rope)

# for line in puzzleList :
#     instruction = line[0]
#     for i in range(int(line[2:])) :
#         for indexRope, ropePart in enumerate(rope) :
#             if indexRope == len(rope)-1 :
#                 break

#             HcolPos = int(ropePart[:ropePart.find(";")])
#             HlinePos = int(ropePart[ropePart.find(";")+1:])

#             TcolPos = int(rope[indexRope+1][:rope[indexRope+1].find(";")])
#             TlinePos = int(rope[indexRope+1][rope[indexRope+1].find(";")+1:])

#             HcolPos = HcolPos + 1
#             HlinePos = HlinePos+1
#             TcolPos = TcolPos+2
#             TlinePos = TlinePos+2

#             HPos = str(HcolPos) + ";" + str(HlinePos)
#             TPos = str(TcolPos) + ";" + str(TlinePos)

#             rope[indexRope] = HPos
#             rope[indexRope+1] = TPos
# print(rope)
# str = "12345"
# str.replace()
# print(str)
# l = ["1","2"]
# for x in l :
#     tail = l[1]
#     tail = 3
# print(l)

def showMe(list) :
    maxc = 0
    maxl = 0
    minC = 0
    minL = 0
    showL = []
    for e in list :
        lCo = int(e[:e.find(";")])
        cCo = int(e[e.find(";")+1:])
        if lCo >= maxl :
            maxl = lCo+1
        if cCo >= maxc :
            maxc = cCo+1

        if lCo <= minL :
            minL = lCo-1
        if cCo <= minC :
            minC = cCo+1
        lineNb = 0
        colNb = 0
        if abs(minL) > maxl :
            lineNb = abs(minL)*2
        else :
            lineNb = maxl*2
        
        if abs(minC) > maxc :
            colNb = abs(minC)*2
        else :
            colNb = maxc*2

    for i in range(lineNb) :
        showL.append("")
    for ix in range(lineNb) :
        for ii in range(colNb) :
            showL[ix] += ". "
    print(showL)
    print(lineNb, colNb)
    for co in list :
        idxC = abs((colNb//2 + int(co[co.find(";")+1:]))*2) #4
        idxL = abs(lineNb//2 + int(co[:co.find(";")])) #1
        print("ma b", idxC, idxL)
        newstr = showL[idxL][:idxC] + "#" + showL[idxL][idxC+1:] 
        showL[idxL] = newstr
    showL.reverse()
    with open("Advent Of Code 2022\Day 9\Try.txt", "w") as f:
        for indexx, line in enumerate(showL) :
            if indexx == 0 :
                string = "  "
                loopCounter = 0
                for i in range(-len(line)//4, len(line)//4) :
                    if loopCounter == (len(line))//2 :
                        break
                    if -1 < i < 10 :
                        string += " "
                    string += str(i)
                    loopCounter += 1
                print(string)
                f.write(string)
            else :
                w = indexx*-1 + len(showL)//2
                if -1 < int(w) < 10 :
                    print(" " + str(w) + " " + line)
                    f.write("\n" + " " + str(w) + " " + line)
                else :
                    print(str(w) + " " + line)
                    f.write("\n" + str(w) + " " + line)
        f.write("\n")
        for e in list :
            stringgg = str(e) + " "
            f.write("\n" + stringgg)
            
listf = ["-6;-3"]
# for i in range(10) :
#     listf.append(str(random.randint(-5,0)) + ";" + str(random.randint(-5,0)))
print(listf)
showMe(listf)

def showMe(list, plus) :
    maxc = 11
    maxl = 11
    showL = []
    for e in list :
        if int(e[:e.find(";")]) >= maxl :
            maxl = int(e[:e.find(";")])+1
        if int(e[e.find(";")+1:]) >= maxc :
            maxc = int(e[e.find(";")+1:])+1
    for i in range(maxl) :
        showL.append("")
    for ix in range(maxl) :
        for ii in range(maxc) :
            showL[ix] += "."
    if plus == "+" :
        for index, co in enumerate(list) :
            stringg = str(index)
            if index == 0 :
                stringg = "H"
            idxC = int(co[co.find(";")+1:]) #4
            idxL = int(co[:co.find(";")]) #1
            newstr = showL[idxL][:idxC] + stringg + showL[idxL][idxC+1:] 
            showL[idxL] = newstr
        showL.reverse()
    else :
        for co in list :
            idxC = int(co[co.find(";")+1:]) #4
            idxL = int(co[:co.find(";")]) #1
            newstr = showL[idxL][:idxC] + "#" + showL[idxL][idxC+1:] 
            showL[idxL] = newstr
    showL.reverse()
    for line in showL :
        print(line)