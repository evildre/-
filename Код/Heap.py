class Heap:
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.heap = [None] * MAX_SIZE
        self.size = 0
        print('Создаём дерево. На данный в нём не хранится ни одного элемента.')

    @staticmethod
    def get_parent(index):  # метод, возвращающий индекс родителя
        return (index - 1) // 2

    @staticmethod
    def get_left_child(index):  # метод, возвращающий индекс правого ребёнка
        return index * 2 + 1

    @staticmethod
    def get_right_child(index):  # метод, возвращающий индекс левого ребёнка
        return index * 2 + 2

    def insert(self, value):  # добавляем элемент в дерево
        if self.size >= self.MAX_SIZE:  # проверяем, возможно ли ещё добавить элемент в дерево
            print('Вы хотите добавить больше элементов, чем максимальный размер дерева!')
            return -1
        self.heap[self.size] = value
        self.size += 1
        print(
            f'Добавил элемент {value} в наше дерево. Теперь размер дерева = {self.size}')
        self.sift_up(self.size - 1)

    def extract_min(self):
        if self.size == 0:
            print('В дереве нет ни одного элемента')
            return
        print(f'Удаляю наименьший элемент {self.heap[0]} из дерева.')
        min_element = self.heap[0]
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], None
        print(
            f'Поставил последний элемент дерева {self.heap[0]} на место наименьшего.')
        self.size -= 1
        print(f'Удалил наименьший элемент. Размер дерева: {self.size}')
        print(f'Дерево: {self}')
        self.sift_down(0)
        return min_element

    def sift_up(self, index):
        parent = self.get_parent(index)
        while index > 0 and self.heap[parent] > self.heap[index]:
            print(
                f'Просеиваю вверх элемент. На данный момент элемент стоит на позиции {index}')
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = self.get_parent(index)
            print(
                f'Поднял элемент до позиции {index}. Теперь его дети: {self.heap[self.get_left_child(index)]}, {self.heap[self.get_right_child(index)]}')
        print(f'Дерево: {self}')

    def sift_down(self, index):
        print(f'Просеиваю {self.heap[0]} вниз.')
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        if left >= self.size and right >= self.size:
            print(
                f'Элемент {self.heap[0]} теперь корень дерева. Заканчиваю просеивание.')
            print(f'Дерево: {self}')
            return
        if right >= self.size:
            min_index = left if self.heap[left] < self.heap[index] else index
        else:
            min_index = left if self.heap[left] < self.heap[right] else right
            min_index = min_index if self.heap[min_index] < self.heap[index] else index
        if index != min_index:
            print(
                f'Ребёнок {self.heap[min_index]} оказался меньше элемента {self.heap[index]}, меняю местами.')
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            print(f'Дерево: {self}')
            self.sift_down(min_index)
        else:
            print(
                f'Элемент {self.heap[index]} стоит на своём месте. Заканчиваю просеивание.')
            print(f'Дерево: {self}')

    def __str__(self):
        s = [x for x in self.heap if x!=None]
        return str(s)

    def search(self, x):
        if self.size == 0:
            print('В дереве нет ни одного элемента')
            return
        for i in range(len(self.heap)):
            if self.heap[i] == x:
                return i
        return -1

    def extract_max(self):
        if self.size == 0:
            print('В дереве нет ни одного элемента')
            return
        n = self.size
        maximumElement = self.heap[n // 2]
        print(
            f'Пробегаюсь по нижней половине дереве {[x for x in self.heap[n // 2:] if x!=None]}')
        index = n // 2
        for i in range(n // 2, n):
            if maximumElement < self.heap[i]:
                index = i
                maximumElement = self.heap[i]
        print(f'Максимальный элемент - {maximumElement}')
        if index!=self.size-1:
            self.heap[index], self.heap[self.size-1] = self.heap[self.size-1], None
            self.sift_up(index)
        else:
            self.heap[index] = None
        self.size -= 1
        return maximumElement