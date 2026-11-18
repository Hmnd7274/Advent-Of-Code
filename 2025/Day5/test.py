bl = [(345, 765)]
t = []
for l,k in bl :
    print(l,k)
    t.append((l,k))
# x = bl[0][0]
# y = bl[0][1]
print(bl)
print(t)
for x, y in bl :
    t.remove((x, y))
    print(t)

tab = [(3,6), (4,8), (1,10)]