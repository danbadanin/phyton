class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        strs = ''
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                strs += str(self.data[i][j]) + ' '
            strs += '\n'
        return strs

    def __add__(self, other):
        new_matrix = []
        if len(self.data) != len(other.data):
            return 'Матрицы разные по количеству строк!'
        for i in range(len(self.data)):
            new_matrix.append([])
            if len(self.data[i]) != len(other.data[i]):
                return 'Матрицы разные по количеству столбцов!'
            for j in range(len(self.data[i])):
                new_matrix[i].append(self.data[i][j] + other.data[i][j])
        return Matrix(new_matrix)


my_matrix = Matrix([[1, 3, 4], [6, 7, 8]])
print(my_matrix)

second_matrix = Matrix([[2, 3, 5], [1, 2, 3]])
print(my_matrix + second_matrix)
