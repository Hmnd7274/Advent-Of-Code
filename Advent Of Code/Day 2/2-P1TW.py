with open("./Day 2/D2.txt", "r") as f:
    myList = [line.strip() for line in f]

i = 0
res = str(myList[0])
answer = 0

while i < 2499:

  print(res)

  if res == str("A X"):
    answer = answer + int(4)
    print(answer)

  # if res == str("A Y"):
  #   answer = answer + int(8)
  
  del myList[0]

  res = str(myList[0])

  i = i + 1

print(answer)