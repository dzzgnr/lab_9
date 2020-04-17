import numpy as np
import random
import timeit


def bub_sort(mlist):
    exchange = 0
    count = 0
    lst_item = len(mlist) - 1         #диапазон до предпоследнего элемента
    for i in range(0, lst_item):
        for x in range(0, lst_item):  #начинаем проверки с первого элемента, с каждым сравнением диапазон сокращается    
            count += 1                #количество сравнений
            if mlist[x] > mlist[x + 1]:   #проверка элемента с последующим
                mlist[x], mlist[x + 1] = mlist[x + 1], mlist[x]    #если больше то выполняем замену
                exchange += 1
    print("число сравнений:", count)                    #вывод значения
    print("число обменов:", exchange)                  #вывод значения
    print(" ")

    return list


def selection_sort(array):
    exchanger = 0
    counter = 0
    for i in range(len(array) - 1):          # диапазон до предпоследнего элемента
        counter += 1       #количество сравнений
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:      #задания условия
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]         #если массив J less than M меняем местами
        exchanger += 1                     #количество обменов
    print("число сравнений:", counter)
    print("число обменов:", exchanger)
    return array                      #возвращаем массив


def insertion(data):             #создание функции
    exchanger = 0                #количество перестановок
    counter = 0                 #количество сравнений
    for i in range(len(data)):      
        counter += 1
        j = i - 1
        key = data[i]                   #Присвоение элемента ключу, как позже сохранится на новом месте     
        while data[j] > key and j >= 0:  #задания условия при которой будет происходить замена
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key            #замена элементов
        exchanger += 1
    print("число сравнений:", counter - 1)
    print("чсло обменов:", exchanger)
    return data

while True:
    while True:
        try:
            choose = int(input("bubble sort - 1,selection sort - 2,insertion sort - 3,ваш вибор: "))
            if choose <= 3:
                break
            else:
                choose = int(input("bubble sort - 1,selection sort - 2,insertion sort - 3,ваш вибор: "))
                break
        except ValueError:
            print("только цифры")
    flag = input(
        "Если вы хотите рандомизировать входные данные, нажмите «Enter». Для ввода вручную нажмите любую другую клавишу: ")
    print("")
    if flag == "":
        while True:
            try:
                b = int(input("Введите количество которая будет генерироваться: "))
                break
            except ValueError:
                print("Только цифры")
        a = np.zeros(b, dtype=int)
        while True:
            try:
                d1 = int(input('Левая грань: '))  #задания границ
                d2 = int(input('Правая грань: ')) #задания границ
                break
            except ValueError:
                print("только цифри")
        for i in range(b):
            a[i] = random.randint(d1, d2)

    else:
        while True:
            try:
                b = int(input("Введите количество которая будет генерироваться: "))
                if b <= 30:
                    break
                else:
                    b = int(input("Введите количество которая будет генерироваться: "))
            except ValueError:
                print("только цифры")
        a = np.zeros(b, dtype=int)
        for i in range(b):
            a[i] = int(input(f'Enter {i + 1} element: '))

    if choose == 1:                #задания условия на выбор метода сортировки
        print("Старый список", a)
        print(" ")

        new = bub_sort(a)
        print("Отсортирован от меньшего к большему", new)
        print(" ")

        s = np.array(a)
        x = s[::-1]
        print("От большего к меньшему", x)
        print(" ")



    if choose == 2:                                    #задания условия на выбор метода сортировки
        print("Старый список", a)
        print(" ")
        new = selection_sort(a)
        print("Отсортирован от меньшего к большему", new)
        print(" ")
        s = np.array(a)
        x = s[::-1]                                 #с помощью среза выводим элементы наоборот
        print("От большего к меньшему", x)
        print(" ")


    if choose == 3:                              #задания условия на выбор метода сортировки
        print("Старый список", a)
        print(" ")
        new = insertion(a)
        print("отсортирован от меньшего к большему", new)
        print(" ")
        s = np.array(a)
        x = s[::-1]                                         #с помощью среза выводим элементы наоборот
        print("От большего к меньшему", x)
        print(" ")

    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(f"Программа выполнялась {t} секунд")
    print(" ")
    if input('Нажмите "Enter"  для перезагрузки: ') == '':
        continue
    break
