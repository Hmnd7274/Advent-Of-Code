#54320
fichier = open("Day2\\text.txt", "r")
jsp = fichier.readlines()
a = 0
for i in jsp :
    jsp[a] = i.strip()
    a += 1
x = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
#jsp = ["Game 1: 12 blue; 2 green, 13 blue, 19 red; 13 red, 3 green, 14 blue"]

power = 0
p = 0

print(len(jsp[0]))
for element in jsp :
    red = 0
    green = 0
    blue = 0
    mRed = 0
    mGreen = 0
    mBlue = 0
    print("element =", element)
    ind = 0
    letterI = 0
    for letter in element :
        if letter == ";" or letterI == len(element) - 1 :
            if red > mRed :
                mRed = red
            if green > mGreen :
                mGreen = green
            if blue > mBlue :
                mBlue = blue
            red = 0
            green = 0
            blue = 0
            #print("RESET")

        elif letter.isdigit() :
            #print("letter =", letter)
            if not element[ind + 1].isdigit() and not element[ind - 1].isdigit() :
                if element[ind + 2] == "r" :
                    red += int(letter)
                    #print("red =", red)
                if element[ind + 2] == "g" :
                    green += int(letter)
                    #print("green =", green)
                if element[ind + 2] == "b" :
                    blue += int(letter)
                    #print("blue =", blue)

            if element[ind - 1].isdigit() :
                letter = int(str(element[ind - 1]) + str(letter))
                #print("letterrrrrrrrrrrrr =", letter)
                if element[ind + 2] == "r" :
                    red += int(letter)
                    #print("red =", red)
                if element[ind + 2] == "g" :
                    green += int(letter)
                    #print("green =", green)
                if element[ind + 2] == "b" :
                    blue += int(letter)
                    #print("blue =", blue)
        if letterI == len(element) - 1 :
            print("POWER HAS CHANGED =", power, "+", mRed, "*", mGreen, "*", mBlue)
            power += (mRed * mGreen * mBlue)
            p += 1
        letterI += 1
        ind += 1
    print("Power =", power)
    print("p =", p)