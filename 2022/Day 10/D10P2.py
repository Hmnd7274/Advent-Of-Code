with open("Advent Of Code 2022\\Day 10\\D10.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

def drawPx(x, cycle) :
    px = "."
    if cycle in [i for i in range(x-1,x+2)] :
        px = "#"
    return px

cycle = 0
x = 1
listAnsw = []
listImage = []
imageLineIndex = 0
for u in range(6) :
    listImage.append("")

for indexInput, inputLine in enumerate(puzzleList) :
    if inputLine.startswith("addx") :
        for i in range(2) :
            if cycle not in listAnsw :
                imageLineIndex = (cycle-1) // 40
                if imageLineIndex == -1 :
                    imageLineIndex = 0
                else :
                    listAnsw.append(cycle)
                    listImage[imageLineIndex] += drawPx(x, (cycle-1) % 40)
            cycle += 1

        if cycle not in listAnsw :
            imageLineIndex = (cycle-1) // 40
            if imageLineIndex == -1 :
                imageLineIndex = 0
            else :
                listAnsw.append(cycle)
                listImage[imageLineIndex] += drawPx(x, (cycle-1) % 40)

        x += int(inputLine[inputLine.find(" ")+1:])
    else :
        if cycle not in listAnsw :
            imageLineIndex = (cycle-1) // 40
            if imageLineIndex == -1 :
                imageLineIndex = 0
            else :
                listAnsw.append(cycle)
                listImage[imageLineIndex] += drawPx(x, (cycle-1) % 40)
        cycle += 1
for e in listImage :
    print(str(e) + " " + str(len(e)))