from random import *
s=[]
pos=[]
neg=[]
nol=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

def vahetus(a:int,b:int):
    """Меняет местами a и b
    :param int a: минимальное число, которое больше чем максимальное
    :param in b: максимальное число, которое меньше чем минимальное
    :rtype: int,int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """генерирует список от минимального до максимального
    :param n int: Кол-во чисел в списке
    :param loend list: Список
    :param a int: Минимальное число
    :param b int: Максимальное число
    """
    for i in range(n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:list,nol:list):
    """Создает списки с положительными,отрицательными и нулевыми числами
    :param loend list: список
    :param p list: Создает список положительных чисел
    :param n list: Создает список негативных чисел
    :param nol list: Создает список нулевых чисел
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend):
    """считывает среднее 
    :param loend list: список
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """добавляет среднее в список и сортирует
    :param loend list: список чисел
    :param el float: среднее дробное число
    """
    loend.append(el)
    loend.sort()

