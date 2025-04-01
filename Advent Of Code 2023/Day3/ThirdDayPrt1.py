fichier = open("Day3/example.txt", "r")
tableau = fichier.readlines()
sum = 0

a = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
symbols = ['*', '#', '+', '$']

#for element in tableau :
#    element = element.strip()
#    for letter in element :
#        if letter not in a and letter not in symbols :
#            symbols.append(letter)
#
#print(symbols)

ligneI = 0

for ligne in tableau :
    print("ligne", ligne)
    letterI = 0
    nb = None
    ligne = ligne.strip()

    if ligneI != 0 :
        ligneP = tableau[ligneI - 1]
        print("ligneP =", ligneP)
    if ligneI != len(tableau) - 1 :
        ligneS = tableau[ligneI + 1]
        print("ligneS =", ligneS)

    for letter in ligne :
        print("letter =", letter)

        if letter in symbols :
            print("symbol =", letter)
            print(ligneP[letterI].isdigit())

            if ligneP[letterI].isdigit() :
                print(ligneP[letterI - 1])

                for a in range(len(ligneP) - letterI) :

                    if nb == None and ligneP[letterI - a].isdigit() :
                        nb = str(ligneP[letterI - a])
                        print("nombre =",nb)
                    
                    elif ligneP[letterI - a].isdigit() :
                        print("grj", nb)
                        nb = str(ligneP[letterI - a]) + nb

            #for a in range(len(ligneP)) :
#
            #    if ligneP[letterI - a].isdigit() :
#
            #        if nb != None :
            #            nb = int(str(ligneP[ligneI - a - 1]) + str(ligneP[ligneI - a]))
            #        
            #        else :
            #            nb = ligneP[ligneI - 1]

        letterI = 0

    ligneI += 1