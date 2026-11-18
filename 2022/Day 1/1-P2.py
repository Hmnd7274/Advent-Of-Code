with open("Advent Of Code 2022\Day 1\D1.txt") as f:
  lines = str(f.read())

rawInventories = lines.split("\n\n")
inventories = []

for i in rawInventories:
  currentInventory = []

  for x in i.splitlines():
    currentInventory.append(int(x))

  inventoryCalories = sum(currentInventory)
  inventories.append(inventoryCalories)

answer = int(0)

for i in range(3):
  answer = answer + (max(inventories))
  inventories.remove(max(inventories))

print(answer)