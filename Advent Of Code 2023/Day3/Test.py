def findNumber(ligne, index) :
    print(ligne[index].isdigit())
    if ligne[index].isdigit() :
        nb = ligne[index]
        a = 1
        while a - 1 < index :
            print("letter=", ligne[index - a])
            if ligne[index - a].isdigit() :
                print(ligne[index - a])
                nb = str(ligne[index - a]) + nb
                print("nb=",nb)
            a += 1
        a = 1
        print("longueur = ",len(ligne) - index)
        while a < len(ligne) - index :
            print("letter=", ligne[index + a],"a=", a)
            if ligne[index + a].isdigit() :
                print(ligne[index + a])
                nb = nb + str(ligne[index + a])
                print("nb=",nb)
            a += 1
        
    return nb

x = ".34567.....999..."
print(findNumber(x, 5))