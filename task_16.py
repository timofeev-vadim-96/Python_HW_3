# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# Очевидно, что в массиве от 1...N искомое число повторится либо один раз, либо 0. Подозрительно простая задача,
# поэтому я решил искать хотя бы цифру, а не число... Например, цифра 5 имеется в числах: 5, 15, 25 и т.д.
N = int(input('Введите размер списка: '))
list_1 = [i for i in range(1, N+1)]
find_N = input('Введите искомую цифру: ')
output_string = str(list_1)
counter = 0
for i in output_string:
    if i == find_N: counter+=1
print(f'{list_1}\n-> {counter}')