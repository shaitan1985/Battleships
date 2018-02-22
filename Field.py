from random import randint
from itertools import combinations_with_replacement as com

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


    def get_free_places(self):
        n = self.n
        # обработка соседних координат
        temp_mtr = [[self.matrix[i][j] for i in range(n)] for j in range(n)]

        for i in
        """
         если обработку закомментить,
         то будет все работать,
         но корабли могут стоять вплотную
        """
        free = [(i, j) for i in range(n) for j in range(n) if self.matrix[i][j] == 0 ]

        return free


    def locate_ship(self, matrix, n, level):
        pos = randint(0, 1) #рандомное направление
        temp_mtr = [[matrix[i][j] for i in range(n)] for j in range(n)]
        free = get_free_places() # свободные координаты
        x = (randint(1, n), randint(1, n))
        # расположение
        if x in free:
                for k in range(level):
                col = x[0] if pos else x[0] + k
                row = x[1] + k if pos else x[1]
                print(col, row)
                try:
                    # Если выходим за пределы поля
                    tmp_item = temp_mtr[col][row]
                except IndexError:
                        return False
                if tmp_item:
                    return False
                temp_mtr[col][row] = 1
        self.draw_field(temp_mtr)
        self.matrix = temp_mtr
        self.draw_field(self.matrix)
        return True





    def get_new_coords(self):
        n = self.n
        for i in range(1, 5):
            level, count = 5 - i, i
            while count:
                if self.locate_ship(self.matrix, n, level):
                    count -= 1



        return self.matrix