fichier = open("text.txt", "r")
jsp = fichier.readlines()
a = 0
for i in jsp :
    jsp[a] = i.strip()
    a += 1
x = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
#jsp = ["Game 1: 12 blue; 2 green, 13 blue, 19 red; 13 red, 3 green, 14 blue"]

letterI = 0
red = 0
green = 0
blue = 0
mRed = 12
mGreen = 13
mBlue = 14
notPossible = 0
elemNumber = 1

print(len(jsp[0]))
for element in jsp :
    red = 0
    green = 0
    blue = 0
    print("element =", element)
    ind = 0
    for letter in element :
        if letter == ";" :
            red = 0
            green = 0
            blue = 0
            print("RESET")
        elif letter.isdigit() :
            print("letter =", letter)
            if not element[ind + 1].isdigit() and not element[ind - 1].isdigit() :
                if element[ind + 2] == "r" :
                    red += int(letter)
                    print("red =", red)
                if element[ind + 2] == "g" :
                    green += int(letter)
                    print("green =", green)
                if element[ind + 2] == "b" :
                    blue += int(letter)
                    print("blue =", blue)
                if red > mRed :
                    notPossible += elemNumber
                    print("notPossible =", notPossible)
                    break


                if green > mGreen :
                    notPossible += elemNumber
                    print("notPossible =", notPossible)
                    break


                if blue > mBlue :
                    notPossible += elemNumber
                    print("notPossible =", notPossible)
                    break


            if element[ind - 1].isdigit() :
                letter = int(str(element[ind - 1]) + str(letter))
                print("letterrrrrrrrrrrrr =", letter)
                if element[ind + 2] == "r" :
                    red += int(letter)
                    print("red =", red)
                if element[ind + 2] == "g" :
                    green += int(letter)
                    print("green =", green)
                if element[ind + 2] == "b" :
                    blue += int(letter)
                    print("blue =", blue)
                if red > mRed :
                    notPossible += elemNumber
                    print("notPossible =", notPossible)
                    break
                if green > mGreen :
                    notPossible += elemNumber
                    print("notPossible =", notPossible)
                    break
                if blue > mBlue :
                    notPossible += elemNumber
                    print("notPossible =", notPossible)
                    break
        ind += 1
        #print("indice =", ind)
    elemNumber += 1
    print("notPossible =", notPossible)
hehe = 0
for i in range(1, 101) :
    print(i)
    hehe += i
print(hehe - notPossible)