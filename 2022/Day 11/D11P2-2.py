import re
import operator
import gmpy2
import timeit
import time
import math


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
pattern2 = r"([+*-])"
compiled1 = re.compile(pattern1)
compiled2 = re.compile(pattern2)

# operatorr = "old * old"[4]
# answer = operators[operatorr](3, 3)
# print(answer)

# Enregistrer chaque singe avec ses items, son opération, son test
# Faire opérer les singes dans l'ordre

def smallestModuloNumber(currentNumber: int, listDivision: list[int]) -> int:
    lcm = math.lcm(*listDivision)  # PPCM de tous les diviseurs
    return currentNumber % lcm

def findNewModuloNumber(currentNumber: int, listDivision: list, a):

    listRestesIni = []
    for e in listDivision :
        listRestesIni.append(currentNumber % e)
    i = -1
    maman = time.process_time()
    while True :
        i += 1
        if i % listDivision[0] == listRestesIni[0] :
            if i % listDivision[1] == listRestesIni[1] :
                if i % listDivision[2] == listRestesIni[2] :
                    if i % listDivision[3] == listRestesIni[3] :
                        break
    # print(i)
    if time.process_time() - maman> a:
        a = time.process_time() - maman
    return i, a

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


def operateItem(operation: str, item: str, highestTimeInFunction, highestNumber):
    item = int(item[0]) # Transforme le premier item de la liste en int
    answer = 0
    operatorr = findOperator(operation) # Trouve l'opérateur
    if operation.count("old") == 2 : # Si old ? old
        secondArg = item
    else :
        secondArg = int(re.findall(compiled1, operation)[-1])
    answer = int(operatorr(item, secondArg)) # Applique l'opération et la stock dans answer

    
    if answer > highestNumber :
        highestNumber = answer

    # maman = time.process_time()
    
    answer = smallestModuloNumber(answer, listDivision)

    # if time.process_time() - maman> highestTimeInFunction:
    #     highestTimeInFunction = time.process_time() - maman

    # answer /= 3
    # print("important", operatorr, "   ", item, "   ", secondArg, "   ", answer)
    return int(answer), highestTimeInFunction, highestNumber

def operateItemDebug(operation: str, item: str):

    item = int(item[0]) # Transforme le premier item de la liste en int
    answer = 0

    if operation.count("old") == 2 : # Si old ? old
        secondArg = item
    else :
        secondArg = int(re.findall(compiled1, operation)[-1])


    ope = re.findall(compiled2, operation)[-1]
    if ope == "+" :
        answer = item + secondArg
    elif ope == "-" :
        answer = item - secondArg
        
    elif ope == "*" :
        start5 = time.process_time()

        answer = item * secondArg

    # answer = int(operatorr(item, secondArg)) # Applique l'opération et la stock dans answer

    # print("time to do the first code snippets", time.process_time() - start)
    
    # answer /= 3
    # print("important", operatorr, "   ", item, "   ", secondArg, "   ", answer)
        print("time to do do the function:", time.process_time() - start5)

    return answer

monkeysList = []
# listDivision = [23, 19, 13, 17]
listDivision = []

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
        test2 = re.findall(compiled1, line)
        monkeysList[-1]["Test"] = test[-1]
        listDivision.append(int(test2[-1]))

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

roundsNumber = 10000

highestTime = 0
highestTimeInFunction = 0
highestNumber = 0

end = False

startStart = time.process_time()
for x in range(roundsNumber) :
    # if end :
    #     break
    for monkey in monkeysList :
        # if end :
        #     break
        itemsNumber = len(monkey["Items"])
        monkey["InspectsNumber"] += itemsNumber
        for i in range(itemsNumber):
            # start = time.process_time()

            # if end :
            #     break

            # start2 = time.process_time()
            # start3 = time.process_time()

            start = time.process_time()

            operatedItem, highestTimeInFunction, highestNumber = operateItem(monkey["Operation"], monkey["Items"], highestTimeInFunction, highestNumber)

            start2 = time.process_time()
            # print(start2 - start)

            if start2 - start > highestTime :
                highestTime = start2 - start

            # if timeit.timeit(stmt=lambda: operateItem(monkey["Operation"], monkey["Items"]), number = 1) >= 0.05 :
            #     operateItemDebug(monkey["Operation"], monkey["Items"])
            #     # print(time.process_time() - start)
            #     end = True
            # print("time to do first:", time.process_time() - start3)
            

            monkeyToSendTo = getMonkeyToSendTo(monkey["Test"], monkey["true"], monkey["false"], int(operatedItem))

            # if timeit.timeit(stmt=lambda: (getMonkeyToSendTo(monkey["Test"], monkey["true"], monkey["false"], int(operatedItem))), number = 1) >= 0.005 :
                
            #     print("okeeeeeeee")
            #     end = True

            # print("time to do the two:", time.process_time() - start2)
            
            # start = time.process_time()
            # # your code here    
            # print(time.process_time() - start)

            # print("throwed ", operatedItem, " from ", monkey["MonkeyNumber"]
            #     , " to Monkey ", monkeyToSendTo, " cause ", monkey["Test"])


            monkeysList[monkeyToSendTo]["Items"].append(operatedItem) # ajouter l'item au bon monkey et retirer l'item

            monkey["Items"].pop(0)

            # print("time to do all of the hard work:", time.process_time() - start)

    if x % 100 == 0:
        print(x)
        print("HIGHEST :", highestTime)
        print("HIGHESTTIMEINFUNCTION :", highestTimeInFunction)
        print("HIGHESTNUMBER :", highestNumber)
        print("time elapsed for this round:", time.process_time() - startStart)
        # startStart = time.process_time()
        for monkey in monkeysList :
            print("insp numb = ", monkey["InspectsNumber"], " Items:", monkey["Items"])
print("OMG", time.process_time() - startStart)

print("\n")

mostInspects = 0
secondMostInspects = 0

for monkey in monkeysList :
    if monkey["InspectsNumber"] > mostInspects :
        secondMostInspects = mostInspects
        mostInspects = monkey["InspectsNumber"]
    if mostInspects != monkey["InspectsNumber"] and monkey["InspectsNumber"] > secondMostInspects :
        secondMostInspects = monkey["InspectsNumber"]

    # print(monkey["Items"], monkey["InspectsNumber"])
    print("insp numb = ", monkey["InspectsNumber"], " Items :", monkey["Items"])


print(mostInspects, secondMostInspects)
print(mostInspects * secondMostInspects)

print(listDivision)