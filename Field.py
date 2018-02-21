from random import randint

class Field(object):


    def __init__(self):
        self.n = 11
        n = self.n
        matrix = [[0 for j in range(n)] for i in range(n)]
        matrix[0][0] = "  "
        for i in range(1, n):
            matrix[i][0] = " АБВГДЕЖЗИК"[i]
            matrix[0][i] = (" " + str(i)) if i != 10 else str(i)
        self.matrix = matrix


    def draw_field(self):
        n = self.n
        t_str = " "
        [print(t_str.join([str(self.matrix[j][i]) for j in range(n)]))
                                            for i in range(n)]


    def locate_ship(matrix, n, level):
        pos = randint(1)
        temp_mtr = [[matrix[i][j] for i in range(n)] for j in range(n)]
        free = [(i, j) for i in range(n) for j in range(n) if matrix[i][j] == 0 ]
        x = (randint(1, n), randint(1, n))
        if x in free:
            for k in range(level):
                tmp_item = temp_mtr[x[0]+k],[x[1]] if pos else temp_mtr[x[0]],[x[1]+k]
                if tmp_item:
                    return None
                tmp_item = 1
        matrix = temp_mtr
        return True





    def get_new_coords(self):
        n = self.n
        matrix = self.matrix
        for i in range(1, 5):
            level, count = 5 - i, i
            while count:
                print(matrix,'\n', n, level)
                if self.locate_ship(matrix, n, level):
                    count -= 1



        return self.matrix