with open("./Day 2/D2.txt") as f:
  lines = f.readlines()
  list = [line.strip() for line in f]
  # first_line = line.split('\n', 1)[0]
  # second_line = line.split('\n', 2)[0]
  # third_line = line.split('\n', 3)[0]

# first_line = str(line[0])
# second_line = str(line[1])
# third_line = str(line[2])
# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors


answer = int(0)
chelou = 0
lineNumber = int(-1)
x = 1
marche = 0

for i in range(2500):

  temp = str(lines[lineNumber])

  lineNumber = lineNumber + int(1)

  if x == 1:
    marche = marche + 1

  if temp == str("A X"):
    answer = answer + int(4)

  if temp == str("A Y"):
    answer = answer + int(8)

  else:
    chelou = chelou + 1

  print(temp)


# print(lineNumber)
print(answer)
print(chelou)
print(marche)
print(list)

# print(463 * 4 + 310 * 8)