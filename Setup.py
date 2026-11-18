import os
def createFolders(startNumb, lastNumb, year) :
    for i in range(startNumb, lastNumb+1) :
        path = str(year) + "./Day " + str(i)
        os.mkdir(path)

def createFiles(startNumb, lastNumb, year) :
    for i in range(startNumb, lastNumb+1) :
        p = str(year) + "./Day " + str(i) + "/"
        path = p + "D" + str(i)
        open(path + ".txt", "w")
        open(path + "P1.py", "w")
        open(path + "P2.py", "w")
        open(p + "test.py", "w")
        toWrite = "with open(\"Advent Of Code " + year + "\\\\Day " + str(i) + "\\\\D" + str(i) + ".txt\", \"r\") as f:\n    puzzleList = [line.strip() for line in f]\n\n"
        with open(path + "P1.py", "w") as f :
            f.write(toWrite)
        with open(path + "P2.py", "w") as f :
            f.write(toWrite)

# createFolders(8, 25, 2022)
# createFiles(11, 11, 2022)