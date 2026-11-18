import timeit
import cython
import numpy
import math
import timeit
import time

# dict1 = {"toto": 3}
# def a(dict2) :
#     dict2["tata"] = 4
#     print(dict2)
# a(dict1)
# print(dict1)

# a = "5+5"
# print(timeit.timeit(a))
# def a(num1, num2) :
#     return num1*num2
# def b(num1, num2) :
#     return numpy.multiply(num1, num2)

# print(timeit.timeit(lambda: a(555555577777777555555577777777555555577777777555555577777777, 5555555777777775555555777777775555555777777775555555777777777777777777888888888), number=1))
# print(timeit.timeit(lambda: b(555555577777777555555577777777555555577777777555555577777777, 5555555777777775555555777777775555555777777775555555777777777777777777888888888), number=1))

def printRestes(x, listDivision) :
    malist = []
    for w in listDivision :
        malist.append(x % w)
    print(malist)

a = 567857997654567890987654345678987657897698098098887655432
b = 0

listDivision = [23, 19, 13, 17]
listRestesIni = [3, 1, 0, 15]

printRestes(a, listDivision)


def smallestModuloNumber(currentNumber: int, listDivision: list[int]) -> int:
    lcm = math.lcm(*listDivision)  # PPCM de tous les diviseurs
    return currentNumber % lcm

def findNewModuloNumber(currentNumber: int, listDivision: list):
    listRestesIni = []
    for e in listDivision :
        listRestesIni.append(currentNumber % e)
    ppcm = math.lcm(*listDivision)
    i = 0
    while True :
        i += ppcm
        if i % listDivision[0] == listRestesIni[0] :
            if i % listDivision[1] == listRestesIni[1] :
                if i % listDivision[2] == listRestesIni[2] :
                    if i % listDivision[3] == listRestesIni[3] :
                        break
    return i

# print(smallestModuloNumber(a, listDivision))
# printRestes(smallestModuloNumber(a, listDivision), listDivision)

def mul(a) :
    return a*a

            # if timeit.timeit(stmt=lambda: operateItem(monkey["Operation"], monkey["Items"]), number = 1) >= 0.05 :
# print("temps :", timeit.timeit(stmt=lambda: mul(9242899600), number=1))
start = time.process_time()
print(math.lcm(*listDivision))
print(a % math.lcm(*listDivision))
print(time.process_time() - start)