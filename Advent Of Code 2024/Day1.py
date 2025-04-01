file1 = open("puzzleInput.txt")
lines = file1.readlines()
list1 = []
list2 = []
for line in lines :
    li = line.split()
    list1.append(li[0])
    list2.append(li[1])
list1.sort()
list2.sort()
totD = 0
for i in range(len(list1)) :
    totD += abs(int(list1[i]) - int(list2[i]))
print(totD)