from random import randint


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        space = self.max_length()
        result = '\n'.join([' '.join([f'{elem}'.rjust(space) for elem in row]) for row in self.matrix])
        return result

    def max_length(self):
        return len(str(max(map(max, self.matrix))))

    def sum_is_possible(self, other):
        if len(self.matrix) != len(other.matrix):
            return False
        for x, y in zip(self.matrix, other.matrix):
            if len(x) != len(y):
                return False
        return True

    def __add__(self, other):
        assert self.sum_is_possible(other), "Matrices must have the same sizes"
        result = a.matrix.copy()
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] += other.matrix[i][j]
        return Matrix(result)

    @staticmethod
    def generate_matrix(n, m, a, b):
        return [[randint(a, b) for j in range(m)] for i in range(n)]


a = Matrix(Matrix.generate_matrix(3, 3, 1, 100))
b = Matrix(Matrix.generate_matrix(3, 3, 1, 100))
print('Matrix a:', a, sep='\n')
print('----')
print('Matrix b:', b, sep='\n')
c = a + b
print('Result:')
print(c)
