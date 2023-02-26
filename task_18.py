# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import math

N = int(input('Введите размер списка: '))
list_1 = [i for i in range(1, N+1)]
find_N = int(input('Введите число: '))
dif = 0
min_dif = 2147483647 # абсурдно большое значение для сравнения
temp_numb_1 = 0 # 1-е ближайшее число
temp_numb_2 = 0 # 2-е ближайшее число
flag = False # ближайшее число к find_N лишь одно
for i in range(0, len(list_1)):
    dif = find_N - list_1[i]
    if dif == 0: print(f'Введенное число {find_N} присутствует в списке')
    elif min_dif > abs(dif): 
        min_dif = abs(dif)
        temp_numb_1 = list_1[i]
    elif min_dif == abs(dif): 
        flag = True
        temp_numb_2 = list_1[i] 
if flag: print(f'Ближайшие к введенному числу - 2 числа: {temp_numb_1} и {temp_numb_2}')
else: print(f'Ближайшее к введенному числу - число: {temp_numb_1}')


