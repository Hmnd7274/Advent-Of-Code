with open("Advent Of Code 2022\Day 4\D4.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

counter = 0

for pairs in puzzleList :
    firstAss = pairs.split(",")[0]
    secondAss = pairs.split(",")[1]

    FStart, FEnd = firstAss[:firstAss.find("-")], firstAss[firstAss.find("-") + 1:]
    SStart, SEnd = secondAss[:secondAss.find("-")], secondAss[secondAss.find("-") + 1:]

    # print(FStart, FEnd, "||", SStart, SEnd)
    # 2-4 et 3-9 ou 7-10 et 2-9
    # 3-3 | 3-8 ou 3-8 | 7-9
    if (int(FStart) <= int(SStart) and int(FEnd) >= int(SStart)) or (int(FStart) <= int(SEnd) and int(FEnd) >= int(SEnd)) :
        counter += 1
    elif (int(SStart) <= int(FStart) and int(SEnd) >= int(FStart)) or (int(SStart) <= int(FEnd) and int(SEnd) >= int(FEnd)) :
        counter += 1

print(counter)