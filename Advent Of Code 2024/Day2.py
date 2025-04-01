import copy
def Check(li) :
    error = None
    x = True
    croissant = None
    for i in range(len(li) - 1) :
        #Check si différence == 0
        if (int(li[i]) - int(li[i+1])) == 0 :
            error = "difference 0"
            x = False
            break
        #Croissant ou pas

        if int(li[0]) < int(li[1]) :
            croissant = True
        else :
            croissant = False
        #Check si tt le temps croissant

        if croissant :
            if int(li[i]) > int(li[i+1]) :
                error = "difference decroi alors que croissant"
                x = False
                break
        else :
            if int(li[i]) < int(li[i+1]) :
                error = "difference croi alors que decroissant"
                x = False
                break
        #Check si différence de max 3
        if croissant :
            if (int(li[i]) - int(li[i+1])) < -3 :
                error = "incrément de plus de 3 alors que croissant"
                x = False
                break
        else :
            if (int(li[i]) - int(li[i+1])) > 3 :
                error = "ddécrement de moins de -3 alors que croissant"
                x = False
                break
    if x == False :
        print(li, "CHECK FALSE")
        print("error :", error)
    return x

def Replace(line: list) :
    print("STARTING REPLACE :\n")
    for i in range(len(line)) :
        lol = copy.deepcopy(line)
        lol.pop(i)
        print("\nLIGNE",line,"\n",i)
        print("lol",lol)
        if Check(lol) == True :
            return True
    print("REPLACE FALSE")
    return False

file1 = open("pzlinp2.txt")
lines = file1.readlines()
answ = 0
for line in lines :
    li = line.split()
    print(li)
    if Check(li) :
        answ += 1
        print("CHECK TRUE")
    else :
        if Replace(li) :
            answ += 1
            print("REPLACE TRUE")
print(answ)