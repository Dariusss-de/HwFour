# Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

# 1. Разложим число на множители
def getListMult(numN):
    list = []
    listMult = [list.append(i) for i in range(1, numN+1) if numN % i == 0]
    return list


# 2. Составим список простых множителей заданного числа
def primeNum(numN):
    primeList = []
    for i in range(2, numN):
        while numN % i == 0:
            numN /= i
            primeList.append(i)
    return primeList

numN = int(input("Введите натуральное число: "))
list1 = getListMult(numN)
print(f'Множители числа {numN} : {list1}')
list2 = primeNum(numN)
print(f'Простые множители числа {numN} :{list2}')