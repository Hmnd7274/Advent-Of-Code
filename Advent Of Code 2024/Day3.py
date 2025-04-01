import re

file1 = open("puzlinput3.txt")
lines = file1.readlines()
answ = 0
pattern = r"mul\((\d+\,\d+)\)"
pattern2 = r"mul\((\d+)\,(\d+)\)|(do\(\))|(don\'t\(\))"
enable = True
PartTwo = True
for line in lines :
    if not PartTwo :
        print(re.findall(pattern, line))
        for e in re.findall(pattern, line) :
            el = e.split(",")
            for i in range(len(e)) :
                if e[i] == "don't()" :
                    enable = False
                    print("ok")
                if e[i] == "do()" :
                    enable = True
            if enable :
                answ += int(el[0]) * int(el[1])
    else :
        print("TKKKKKKT",re.findall(pattern2, line),"\n")
        for e in re.findall(pattern2, line) :
            for i in range(len(e)) :
                if e[i] == "don't()" :
                    enable = False
                if e[i] == "do()" :
                    enable = True
            if enable :
                if e[0].isdigit() and e[1].isdigit() :
                    answ += int(e[0]) * int(e[1])
                    print("passsssse",e[0], e[1])
            else :
                print("passe pas",e)
print(answ)






#    for i in range(line.count("mul(")) :
#        a = line.find("mul(") + 4
#        for i in range(1) :
#            if a + 10 <= len(line)-1 :
#                if (line[a].isdigit() + line[a+1].isdigit() + line[a+2].isdigit() and line[a+3].isdigit() and (line[a+4] == ",")) :
#                    if (line[a+5].isdigit() and line[a+6].isdigit() and line[a+7].isdigit() and line[a+8].isdigit() and line[a+9].isdigit() and (line[a+10] == ")")) :
#                        answ += int(str(line[a]) + str(line[a+1]) + str(line[a+2]) + str(line[a+3])) * int(str(line[a+5]) + str(line[a+6]) + str(line[a+7]) + str(line[a+8]) + str(line[a+9]))
#                        break
#                    
#            if a + 9 <= len(line)-1 :
#                if (line[a].isdigit() + line[a+1].isdigit() + line[a+2].isdigit() and line[a+3].isdigit() and (line[a+4] == ",")) :
#                    if (line[a+5].isdigit() and line[a+6].isdigit() and line[a+7].isdigit() and line[a+8].isdigit() and (line[a+9] == ")")) :
#                        answ += int(str(line[a]) + str(line[a+1]) + str(line[a+2]) + str(line[a+3])) * int(str(line[a+5]) + str(line[a+6]) + str(line[a+7]) + str(line[a+8]))
#                        break
#
#
#
#            if a + 8 <= len(line)-1 :
#                if (line[a].isdigit() + line[a+1].isdigit() + line[a+2].isdigit() and (line[a+3] == ",")) :
#                    if (line[a+4].isdigit() and line[a+5].isdigit() and line[a+6].isdigit() and line[a+7].isdigit() and (line[a+8] == ")")) :
#                        answ += int(str(line[a]) + str(line[a+1]) + str(line[a+2])) * int(str(line[a+4]) + str(line[a+5]) + str(line[a+6]) + str(line[a+7]))
#                        break
#
#            if a + 7 <= len(line)-1 :
#                if (line[a].isdigit() + line[a+1].isdigit() + line[a+2].isdigit() and (line[a+3] == ",")) :
#                    if (line[a+4].isdigit() and line[a+5].isdigit() and line[a+6].isdigit() and (line[a+7] == ")")) :
#                        answ += int(str(line[a]) + str(line[a+1]) + str(line[a+2])) * int(str(line[a+4]) + str(line[a+5]) + str(line[a+6]))
#                        break
#
#
#
#            if a + 6 <= len(line)-1 :
#                if (line[a].isdigit() and line[a+1].isdigit() and (line[a+2] == ",")) :
#                    if (line[a+3].isdigit() and line[a+4].isdigit() and line[a+5].isdigit() and (line[a+6] == ")")) :
#                        answ += int(str(line[a]) + str(line[a+1])) * int(str(line[a+3]) + str(line[a+4]) + str(line[a+5]))
#                        break
#
#            if a + 5 <= len(line)-1 :
#                if (line[a].isdigit() and line[a+1].isdigit() and (line[a+2] == ",")) :
#                    if (line[a+3].isdigit() and line[a+4].isdigit() and (line[a+5] == ")")) :
#                        answ += int(str(line[a]) + str(line[a+1])) * int(str(line[a+3]) + str(line[a+4]))
#                        break
#
#
#
#            if a + 4 <= len(line)-1 :
#                if (line[a].isdigit() and (line[a+1] == ",")) :
#                    if (line[a+2].isdigit() and line[a+3].isdigit() and (line[a+4] == ")")) :
#                        answ += int(line[a]) * int(str(line[a+2]) + str(line[a+3]))
#                        break
#
#            if a + 3 <= len(line)-1 :
#                if (line[a].isdigit() and (line[a+1] == ",")) :
#                    if (line[a+2].isdigit() and (line[a+3] == ")")) :
#                        answ += int(line[a]) * int(line[a+2])
#                        break
#print(answ)




#for line in lines :
#    for i in range(len(line) - 3) :
#        if str(line[i]) + str(line[i+1]) + str(line[i+2]) + str(line[i+3]) == "mul(" :
#            a = i + 4
#
#
#            if (line[a].isdigit() and (line[a+1] == ",")) :
#                if (line[a+2].isdigit() and (line[a+3] == ")")) :
#                    answ += int(line[a]) * int(line[a+2])
#                if (line[a+2].isdigit() and line[a+3].isdigit() and (line[a+4] == ")")) :
#                    answ += int(line[a]) * int(str(line[a+2]) + str(line[a+3]))
#
#
#
#            if (line[a].isdigit() and line[a+1].isdigit() and (line[a+2] == ",")) :
#                if (line[a+3].isdigit() and line[a+4].isdigit() and (line[a+5] == ")")) :
#
#                    answ += int(str(line[a]) + str(line[a+1])) * int(str(line[a+3]) + str(line[a+4]))
#
#                if (line[a+3].isdigit() and line[a+4].isdigit() and line[a+5].isdigit() and (line[a+6] == ")")) :
#
#                    answ += int(str(line[a]) + str(line[a+1])) * int(str(line[a+3]) + str(line[a+4]) + str(line[a+5]))
#
#
#
#            if (line[a].isdigit() + line[a+1].isdigit() + line[a+2].isdigit() and (line[a+3] == ",")) :
#                if (line[a+4].isdigit() and line[a+5].isdigit() and line[a+6].isdigit() and (line[a+7] == ")")) :
#
#                    answ += int(str(line[a]) + str(line[a+1]) + str(line[a+2])) * int(str(line[a+4]) + str(line[a+5]) + str(line[a+6]))
#
#                if (line[a+4].isdigit() and line[a+5].isdigit() and line[a+6].isdigit() and line[a+7].isdigit() and (line[a+8] == ")")) :
#
#                    answ += int(str(line[a]) + str(line[a+1]) + str(line[a+2])) * int(str(line[a+4]) + str(line[a+5]) + str(line[a+6]) + str(line[a+7]))
#
#
#
#            if (line[a].isdigit() + line[a+1].isdigit() + line[a+2].isdigit() and line[a+3].isdigit() and (line[a+4] == ",")) :
#                if (line[a+5].isdigit() and line[a+6].isdigit() and line[a+7].isdigit() and line[a+8].isdigit() and (line[a+9] == ")")) :
#    
#                    answ += int(str(line[a]) + str(line[a+1]) + str(line[a+2]) + str(line[a+3])) * int(str(line[a+5]) + str(line[a+6]) + str(line[a+7]) + str(line[a+8]))
#
#                if (line[a+5].isdigit() and line[a+6].isdigit() and line[a+7].isdigit() and line[a+8].isdigit() and line[a+9].isdigit() and (line[a+10] == ")")) :
#
#                    answ += int(str(line[a]) + str(line[a+1]) + str(line[a+2]) + str(line[a+3])) * int(str(line[a+5]) + str(line[a+6]) + str(line[a+7]) + str(line[a+8]) + str(line[a+9]))
#print(answ)