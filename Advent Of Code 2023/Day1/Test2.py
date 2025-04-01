a = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tab = "vnirejone2threefzjsfour"

def transformator(word) :
    if word == "one" :
        return 1
    if word == "two" :
        return 2
    if word == "three" :
        return 3
    if word == "four" :
        return 4
    if word == "five" :
        return 5
    if word == "six" :
        return 6
    if word == "seven" :
        return 7
    if word == "eight" :
        return 8
    if word == "nine" :
        return 9

for i in range(len(a) - 1) :
    if tab.find(a[i]) >= 0 :
        print(tab.find(a[i]))
        wordI = tab.find(a[i])
        word = a[i]
        print(a[i])
        if wordI < firstNumberI :
            firstNumber = transformator(word)
        if wordI > lastNumberI :
            lastNumber = transformator(word)