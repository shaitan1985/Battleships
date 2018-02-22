from random import randint
from itertools import product as comb

class Field(object):


    def __init__(self):
        # масив 11, потому чтов 0 индексах имена полей
        self.n = 11

        n = self.n
        matrix = [[0 for j in range(n)] for i in range(n)]
        matrix[0][0] = "  "
        for i in range(1, n):
            matrix[i][0] = " АБВГДЕЖЗИК"[i]
            matrix[0][i] = (" " + str(i)) if i != 10 else str(i)
        self.matrix = matrix


    def draw_field(self, matrix=None):
        # отрисовывает либо матрицу из self либо из параметра
        n = self.n
        matrix = self.matrix if matrix is None else matrix
        t_str = " "
        [print(t_str.join([str(matrix[j][i]) for j in range(n)]))
                                            for i in range(n)]


    def get_coord_tuple(self):
        tmp = []
        tupl = (1, 0, -1)
        itr = comb(tupl, repeat=2)
        for i in range(9):
            while 1:
                try:
                    tmp.append(next(itr))
                except StopIteration:
                    break
        return tmp

    def get_free_places(self):
        n = self.n

        # обработка соседних координат но это дерьмо не пашет
        # список координат смещения от центра занятой точки
        lst_coord = self.get_coord_tuple()
        #
        not_free  = [(i, j) for i in range(1, n) \
                for j in range(1, n) if self.matrix[i][j] != 0 ]
        temp_mtr = [[self.matrix[i][j] for i in range(n)] for j in range(n)]

        print(not_free)
        for item in not_free:
            for ext in lst_coord:
                try:

                    col = item[0] + ext[0]
                    row = item[1] + ext[1]

                    if not col or not row:
                        continue
                    # Если выходим за пределы поля
                    temp_mtr[col][item[1] + ext[1]] = 1
                except IndexError:
                    continue

        self.draw_field(temp_mtr)
        print(temp_mtr, '******************\n')
        """
         если обработку закомментить,
         то будет все работать,
         но корабли могут стоять вплотную
        """
        free = [(i, j) for i in range(n) for j in range(n) if temp_mtr[i][j] == 0 ]
        print(free)
        return free


    def locate_ship(self, matrix, n, level):
        pos = randint(0, 1) #рандомное направление
        temp_mtr = [[matrix[i][j] for i in range(n)] for j in range(n)]
        free = self.get_free_places() # свободные координаты
        x = (randint(1, n), randint(1, n))
        # расположение
        if x in free:
            for k in range(level):
                col = x[0] if pos else x[0] + k
                row = x[1] + k if pos else x[1]
                try:
                    # Если выходим за пределы поля
                    tmp_item = temp_mtr[col][row]
                except IndexError:
                        return False
                if tmp_item:
                    return False
                temp_mtr[col][row] = 1
        self.matrix = temp_mtr
        return True





    def get_new_coords(self):
        n = self.n
        for i in range(1, 5):
            level, count = 5 - i, i
            while count:
                if self.locate_ship(self.matrix, n, level):
                    count -= 1



        return self.matrix