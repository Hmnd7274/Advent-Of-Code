def intToList(int) :
    list = []
    for i in range(len(str(int))) :
        list.append(str(int)[i])
    print(list)

intToList(157)