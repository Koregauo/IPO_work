import numpy as np
def det(matrix):
    return np.linalg.det(matrix)
def res(A, b):
    return np.linalg.solve(A, b)

# Пример матрицы 3x3
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
print("Матрица A:")
print(A)

# Вычисляем определитель матрицы A
det_A = det(A)
print("Определитель матрицы A: ", det_A)

# Определяем вектор b
b = np.array([1, 2, 3])

# Решаем систему уравнений Ax = b
x = res(A, b)
print("Решение системы уравнений Ax = b: ", x)
