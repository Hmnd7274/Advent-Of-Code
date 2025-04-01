with open("./Day 1/D1.txt") as f:
  lines = str(f.read())

rawInventories = lines.split("\n\n")
inventories = []

for i in rawInventories:
  currentInventory = []

  for x in i.splitlines():
    currentInventory.append(int(x))

  inventoryCalories = sum(currentInventory)
  inventories.append(inventoryCalories)

print(max(inventories))
