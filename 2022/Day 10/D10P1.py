with open("Advent Of Code 2022\\Day 10\\D10.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

cycle = 0
x = 1
signalStrength = 0
listAnsw = []
for indexInput, inputLine in enumerate(puzzleList) :
    w = 0
    if inputLine.startswith("addx") :
        for i in range(2) :
            if (cycle-20) % 40 == 0 and cycle not in listAnsw :
                signalStrength += x*cycle
                listAnsw.append(cycle)
                print("cycle:",cycle, "x=", x, "sStrength+=", x * cycle)
            cycle += 1
        if (cycle-20) % 40 == 0 and cycle not in listAnsw :
            signalStrength += x*cycle
            listAnsw.append(cycle)
            print("cycle:",cycle, "x=", x, "sStrength+=", x * cycle)
        x += int(inputLine[inputLine.find(" ")+1:])
    else :
        if (cycle-20) % 40 == 0 and cycle not in listAnsw:
            signalStrength += x*cycle
            listAnsw.append(cycle)
            print("cycle:",cycle, "x=", x, "sStrength+=", x * cycle)
        cycle += 1
print(signalStrength)