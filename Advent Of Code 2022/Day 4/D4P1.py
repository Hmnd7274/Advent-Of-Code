with open("Advent Of Code 2022\Day 4\D4.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

counter = 0

for pairs in puzzleList :
    firstAss = pairs.split(",")[0]
    secondAss = pairs.split(",")[1]

    FStart, FEnd = firstAss[:firstAss.find("-")], firstAss[firstAss.find("-") + 1:]
    SStart, SEnd = secondAss[:secondAss.find("-")], secondAss[secondAss.find("-") + 1:]

    # print(FStart, FEnd, "||", SStart, SEnd)
    # 2-9 et 3-9 ou 3-9 et 2-9
    if (int(FStart) <= int(SStart) and int(FEnd) >= int(SEnd)) or (int(FStart) >= int(SStart) and int(FEnd) <= int(SEnd)) :
        if(int(FStart) == int(SStart) and int(FEnd) == int(SEnd)):
            print("ok")
        counter += 1

print(counter)