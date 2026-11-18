import re
import operator

with open("Day 11\D11.txt", "r") as f:
    puzzleList = [line.strip() for line in f]

operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
}

pattern1 = r"(\d+)"
compiled1 = re.compile(pattern1)

# operatorr = "old * old"[4]
# answer = operators[operatorr](3, 3)
# print(answer)

# Enregistrer chaque singe avec ses items, son opération, son test
# Faire opérer les singes dans l'ordre

def findOperator(operation: str) :
    for key in operators.keys() :
        if key in operation :
            operatorr = operators[key]
    return operatorr

def getMonkeyToSendTo(test: str, trueResult: str, falseResult: str, item: int) :
    # operationn = re.findall(r"\W* (by) \W*", test)[-1]
    numberThatDivides = int(re.findall(compiled1, test)[-1])
    # print(operation)
    monkeyToSendTo = re.findall(compiled1, falseResult)[-1]
    if item % numberThatDivides == 0 :
        monkeyToSendTo = re.findall(compiled1, trueResult)[-1]
    return int(monkeyToSendTo)


def operateItem(operation: str, item: str):
    item = int(item[0]) # Transforme le premier item de la liste en int
    answer = 0
    operatorr = findOperator(operation) # Trouve l'opérateur
    if operation.count("old") == 2 : # Si old ? old
        secondArg = item
    else :
        secondArg = int(re.findall(compiled1, operation)[-1])
    answer = int(operatorr(item, secondArg)) # Applique l'opération et la stock dans answer
    # answer /= 3
    # print("important", operatorr, "   ", item, "   ", secondArg, "   ", answer)
    return int(answer)

monkeysList = []

for line in puzzleList :
    if line[:6] == "Monkey" :
        monkeysList.append({"MonkeyNumber": re.findall(compiled1, line)[-1]})

    if "Starting items:" in line :
        monkeysList[-1]["Items"] = []
        items = re.findall(compiled1, line)
        for item in items :
            monkeysList[-1]["Items"].append(item)

    if "Operation:" in line :
        operation = re.findall(r"new = (.*)", line)
        
        monkeysList[-1]["Operation"] = operation[-1]

    if "Test:" in line :
        test = re.findall(r"Test: (.*)", line)
        monkeysList[-1]["Test"] = test[-1]

    if "true:" in line :
        true = re.findall(r"true: (.*)", line)
        monkeysList[-1]["true"] = true[-1]

    if "false:" in line :
        false = re.findall(r"false: (.*)", line)
        monkeysList[-1]["false"] = false[-1]
    
    monkeysList[-1]["InspectsNumber"] = 0

print("\n")

for e in monkeysList :
    print(e)

roundsNumber = 20
roundsPassed = 0

for x in range(roundsNumber) :
    for monkey in monkeysList :
        itemsNumber = len(monkey["Items"])
        monkey["InspectsNumber"] += itemsNumber
        for i in range(itemsNumber):
            operatedItem = operateItem(monkey["Operation"], monkey["Items"])
            monkeyToSendTo = getMonkeyToSendTo(monkey["Test"], monkey["true"], monkey["false"], int(operatedItem))

            # print("throwed ", operatedItem, " from ", monkey["MonkeyNumber"]
            #     , " to Monkey ", monkeyToSendTo, " cause ", monkey["Test"])

            monkeysList[monkeyToSendTo]["Items"].append(operatedItem) # ajouter l'item au bon monkey et retirer l'item
            monkey["Items"].pop(0)
    roundsPassed += 1
    if roundsPassed % 100 == 0:
        print(roundsPassed)

print("\n")

for monk in monkeysList :
    print("insp numb = ", monk["InspectsNumber"])

mostInspects = 0
secondMostInspects = 0

for monkey in monkeysList :
    if monkey["InspectsNumber"] > mostInspects :
        secondMostInspects = mostInspects
        mostInspects = monkey["InspectsNumber"]
    if mostInspects != monkey["InspectsNumber"] and monkey["InspectsNumber"] > secondMostInspects :
        secondMostInspects = monkey["InspectsNumber"]

    print(monkey["Items"], monkey["InspectsNumber"])

print(mostInspects, secondMostInspects)
print(mostInspects * secondMostInspects)