# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
class Matrix:
    def __init__(self, matrix):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.data = matrix

    def __str__(self):
        result = "\n".join(" ".join(map(str, row)) for row in self.data)

        return result

    def __eq__(self, other):
        if (other, Matrix):
            return self.data == other.data
        return False

    def __add__(self, other):
        result = []
        for i in range(self.rows):
            temp_result = []
            for j in range(self.cols):
                temp_result.append(self.data[i][j] + other.data[i][j])
            result.append(temp_result)
        return Matrix(result)


# Пример использования:


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

m1 = Matrix(matrix1)
m2 = Matrix(matrix2)

print("Первая матрица:")
print(m1)

print("Вторая матрица:")
print(m2)

print(m1 == m2)
m3 = m1+m2
print(m3)
