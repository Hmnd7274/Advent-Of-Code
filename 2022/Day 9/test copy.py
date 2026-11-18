list = ["3;7"]
for l in list :
    l += "7"
    # print(l)

    r = l
    w = int(r[:r.find(";")])
    w += 1
#     l += "6"
# print(list)

# my thing abs(Hlinepos) - abs(Tlinepos) > 1 or abs(Hlinepos) - abs(Tlinepos) < -1 or abs(Hcolpos) - abs(Tcolpos) > 1 or abs(Hcolpos) - abs(Tcolpos) < -1

ans = ['0;0', '1;1', '2;2', '3;1', '4;2', '5;3', '5;4', '5;5', '4;6', '3;7', '2;8', '1;9', '0;10', '-1;9', '-2;8', '-3;7', '-4;6', '-5;5', '-5;4', '-5;3', '-5;2', '-5;1', '-5;0', '-5;-1', '-5;-2', '-4;-3', '-3;-4', '-2;-5', '-1;-6', '0;-7', '1;-8', '2;-9', '3;-10', '4;-11', '5;-11', '6;-11']
maxL = 0
maxC = 0
for e in ans :
    if abs(int(e[:e.find(";")])) > maxL :
        maxL = abs(int(e[:e.find(";")]))
    if abs(int(e[e.find(";")+1:])) > maxC :
        maxC = abs(int(e[e.find(";")+1:]))
showL = []
for i in range(maxL*2 + 1) :
    string = ""
    for x in range(maxC*2 + 1) :
        string += "."
    showL.append(string)
print(len(showL))
print(len(showL[0]))
for el in ans :
    lco = int(el[:el.find(";")])+maxL
    coco = int(el[el.find(";")+1:])+maxC
    print("coords=" + str(lco-maxL), coco-maxC, "  ", lco, coco)
    showL[lco] = showL[lco][:coco] + "#" + showL[lco][coco+1:]
showL[maxL] = showL[maxL][:maxC] + "S" + showL[maxL][maxC+1:]
showL.reverse()
for l in showL :
    print(l)