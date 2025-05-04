import re
with open("Advent Of Code 2022\Day 7\D7.txt", "r") as f:
    puzzleList = [line.strip() for line in f]
print("\n\n\n")
sizeDir = {"": 0}
currentSizeDir = sizeDir
rootDir = {}
currentDir = rootDir
currentPath = ""
stageInDir = 0
instruction = ""
dirName = ""

allPaths = []

allDir = []
ligne = 1
for line in puzzleList :
    if line[0] == "$" :
        if line.find("ls") != -1 :
            instruction = "ls"
        # si "cd" et pas première ligne
        elif line.find("cd") != -1 and line != puzzleList[0]:
            # si retour au dossier d'avant
            if (line.find("..")) != -1:
                # update current path en retirant le dernier dossier   /bjr/fg/okhf -> /bjr/fg
                currentPath = currentPath[:-(len(dirName) + 1)]
                # update current dir en récupérant le dernier dossier de cPath   a/bjr/fg/okhf -> okhf
                dirName = currentPath[currentPath.rfind("/")+1:]
                # actualiser le dictionnaire dans lequel on est
                differentDirInPath = re.findall("\/[a-z]*", currentPath)
                if len(differentDirInPath) == 0 :
                    currentDir = rootDir
                else :
                    for index, dir in enumerate(differentDirInPath) :
                        if index == 0 :
                            currentDir = rootDir[dir[1:]]
                        else :
                            currentDir = currentDir[dir[1:]]
                stageInDir -=1
            # si entrée dans dossier quelconque
            else :
                # currentDir devient le nouveau dossier, et currentPath est update aussi
                dirName = line[5:]
                currentPath += "/" + str(dirName)
                if(currentPath) not in allPaths :
                    allPaths.append(currentPath)
                currentDir = currentDir[dirName]
                stageInDir += 1
            instruction = "cd"
    
    elif instruction == "ls" :
        if line.find("dir") == 0 :
            currentDir[str(line[4:])] = {}
            if not (currentPath+"/"+line[4:] in sizeDir.keys()) :
                sizeDir[currentPath+"/"+line[4:]] = 0
        elif line[0].isdigit() :
            currentDir.update({line[line.find(" ")+1:]: line[:line.find(" ")]})

            size = line[:line.find(" ")]
            # attributting sizes
            dirOPath = re.findall("\/[a-z]*", currentPath)
            string = ""
            if len(dirOPath) == 0 :
                sizeDir[""] += int(size)
            else :
                for index, dir in enumerate(dirOPath) :
                    string += dir
                    if index == 0 :
                        sizeDir[""] += int(size)
                    else :
                        sizeDir[string] += int(size)

    ligne += 1

answer = 0

for key, value in sizeDir.items() :
    if value <= 100000 :
        answer += value
print(answer)