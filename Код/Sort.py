from visual import *

def heapify(a, n, index):
    l = 2*index + 1
    r = 2*index + 2
    maxim = index
    print(f'Просеиваю {a[index]} вниз')
    if (l < n):
        if (a[l] > a[maxim]):
            maxim = l
    if (r < n):
        if(a[r] > a[maxim]):
            maxim = r
    if maxim != index:
        print(f'{a[index]} меньше, чем {a[maxim]}. Меняю местами.')
        a[index], a[maxim] = a[maxim], a[index]
        print(f'Ныненший массив: {a}')
        heapify(a, n, maxim)
    else:
        print(f'{a[index]} стоит на своём месте в куче. Ныненший массив: {a}')
    

def heap_sort(a, flag_want):
    n = len(a)
    for i in range(n//2, -1, -1):
        heapify(a, n, i)
    for fin in range(n-1, -1, -1):
        if flag_want=='y':
            drawtree(deserialize(a[0:fin+1]))
        print(f'Меняю {a[fin]} и {a[0]} местами, {a[0]} теперь стоит на нужном месте в отсортированном массиве.')
        a[0], a[fin] = a[fin], a[0]
        print(f'Новый массив: {a}')
        heapify(a,fin,0)

