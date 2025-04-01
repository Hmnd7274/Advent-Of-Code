#for i in range(100) :
#    pass
#a = "11"
#a = a[0] + str(int(a[0]) + int(a[1])) + a[1]
#print(a)

#for x in range(2) :
#    if x > 0 :
#        a = b
#        b = ""
#        print(" ")
#    else :
#        a = "1"
#        b = ""
#        print("DEBUT")
#
#    print("a", a)
#    print("b", b)
#    
#    for i in range(len(a)) :
#        #print("current nb", a[i])
#        if i == len(a) - 1 :
#            b += "1"
#            #print(b)
#        if i == 0 :
#            b += "1"
#            #print(b)
#        if i > 0 and i < len(a) - 1 :
#            b += str(int(a[i - 1]) + int(a[i]))
#            #print(b)
#    print(b)

max = 10
for x in range(max) :
    if x == 0 :
        a = "1"
        b = "1"

    else :
        a = b
        b = ""

        for i in range(len(a)) :
            if i == 0 :
                b += "1"
            if i > 0 :
                b += str(int(a[i - 1]) + int(a[i]))
            if len(a) == len(b) :
                b += "1"
    
    spaces = ""
    for z in range(max - x) :
        spaces += " "
    print(x, "therme :", spaces, b)
    print("longueur =", len(b))


#       1
#      1 1
#     1 2 1
#    1 3 3 1
#
#