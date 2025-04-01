file1 = open("puzzleInput.txt")
lines = file1.readlines()
list1 = []
list2 = []
for line in lines :
    li = line.split()
    list1.append(li[0])
    list2.append(li[1])

def x(a):
    return a == 1


l = [0,1,1,2]
print(list(filter(x, l)))