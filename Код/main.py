from visual import *
from Sort import *
from Heap import *



print('Дерево какого максимального размера вы хотите?')
size = input()
try:
    size = int(size)
    if size <= 0:
        raise ValueError()

except:
    print('Неверно введены данные!')
    exit()
heap = Heap(size)
print('Введите команду. Как только вы введёте 0, это будет означать, что считывание закончно.')
print('1 - вставить элемент')
print('2 - удалить наименьший элемент')
print('3 - поиск элемента')
print('4 - удалить наибольший элемент')
print('5 - выполнить пирамидальную сортировку массива, который будет считан с клавиатуры (никак не связано с уже хранящимся дерево)')
print('6 - вывести дерево')
print('7 - визуализировать дерево')
command = 'ddd'
while True:
    command = input('Введите команду\n')
    if command == '1':
        print('Какой элемент вы хотите вставить?')
        x = input('x = ')
        try:
            x = int(x)
        except:
            print('Неверно введены данные')
            continue
        heap.insert(x)
    elif command == '2':
        heap.extract_min()
    elif command == '3':
        print('Какой элемент вы хотите найти?')
        x = input('x = ')
        try:
            x = int(x)
        except:
            print('Неверно введены данные')
            continue
        ind = heap.search(x)
        if ind != -1:
            print(f'Индекс элемента - {ind}')
        else:
            print('Элемент отсутствует')
    elif command == '4':
        heap.extract_max()
    elif command == '5':
        a = list(map(int, input(
            'Введите массив чисел, который вы хотите отсортировать (все числа через пробел):\n').split()))
        flag_want = input('Хотите ли вы видеть вывод дерева на каждом шаге? y/n \n')
        heap_sort(a, flag_want)
    elif command == '6':
        print(heap)
    elif command=='7':
        drawtree(deserialize(heap.heap))
    elif command == '0':
        print('Пока!')
        break
    else:
        print('Неверно введена команда')
        continue