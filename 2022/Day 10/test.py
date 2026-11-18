# with open("Advent Of Code 2022\\Day 10\\D10 copy.txt", "r") as f:
#     puzzleList = [line.strip() for line in f]

# cycle = 1
# x = 1
# signalStrength = 0
# for indexInput, inputLine in enumerate(puzzleList) :
#     if inputLine != "noop" :
#         print(int(inputLine[inputLine.find(" ")+1:]))
#         x += int(inputLine[inputLine.find(" ")+1:])
    # if cycle == 140 or cycle == 141:
    #     print(inputLine, indexInput)
    # if inputLine == "noop" :
    #     if ((cycle-20) % 40 == 0) :
    #         signalStrength += x * cycle
    #         print("eheh")
    #         print("cycle:",cycle, "x=", x, "sStrength+=", x * cycle)
    #     cycle += 1
    #     continue
    # else :
    #     for step in range(2) :
    #         if ((cycle-20) % 40 == 0) :
    #             signalStrength += x * cycle
    #             print("cycle:",cycle, "x=", x, "sStrength+=", x * cycle)
    #         cycle += 1
    #     x += int(inputLine[inputLine.find(" ")+1:])
# print("x=",x)
# print(cycle)
# print(signalStrength)

# for i in range(400) :
#     if (i-20) % 40 == 0 :
#         print(i)
cycle = 2
x = 1
print([i for i in range(x-1,x+2)])

if cycle in [i for i in range(x-1,x+2)] :
    print("ok")
print("tsur",0 // 40)
print("moi non",40 // 40)
print(201 // 40)