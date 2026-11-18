
# for line in puzzlelines :
#     max1 = 0
#     max1Index = 0
#     index = 0
#     for char in line :
#         if char.isdigit() :
#             char = int(char)
#             if char > max1 :
#                 max1 = char
#                 max1Index = index
#         index += 1

#     templist = list(line)
#     templist.pop(max1Index)
#     newLine = ''.join(templist)
#     # newLine = line[0:max1Index-1]+line[max1Index:]
#     # print("newline= ", newLine, " length=", len(newLine))
#     max2 = 0
#     max2Index = 0
#     index = 0
#     for char in newLine :
#         if char.isdigit() :
#             char = int(char)
#             if char > max2 :
#                 max2 = char
#                 max2Index = index
#         index += 1
#     if max1Index < max2Index :
#         answerTab.append(str(max1)+str(max2))
#     else :
#         answerTab.append(str(max2)+str(max1))
#     print("max1index =", max1Index, "; max2index =", max2Index)
#     print("les deux max = ", max1, ";", max2, "\n")
# print("1234"[0:len("1234")-1])



    # newline = line[max1BisIndex+1:]

        # max2, max2Index = getMax(newline)

        # print("max1INDEX = ", max1Index, "len = ", len(line))
        # print("newline = ", newline)

            # newline = line[max1BisIndex+1:]

        # newline = line[max1Index+1:]
        # print("max1INDEX = ", max1Index, "len = ", len(line))
        # print("newline = ", newline)
        # max2, max2Index = getMax(newline)
stri = ("234234234234278")
print(len(stri))
print(stri[0:len(stri)-11])
print(len(stri[len(stri)-11:]))
print("")
print(stri[0:len(stri)-11])
print(stri[len(stri)-11:])
print("")

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

max, index = getMaxWith11(stri)
print(getMaxWithI(stri[0:index]+stri[index+1:], 11))
print(stri[0:index]+stri[index+1:])
print("\n")

stri = ("234234234234278")

nb = ""
index = 0
for i in range(11, -1, -1) :
    max, index = getMaxWithI(stri, i)
    nb += str(max)
    stri = stri[0:index]+stri[index+1:]

print(nb)
print(434234234278)