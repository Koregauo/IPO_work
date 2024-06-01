import numpy as np

array_2d = np.random.normal(0, 1, (3, 4))
print("Двумерный массив:\n", array_2d)

# Получаем из этого массива одномерный массив с таким же атрибутом size
array_1d = array_2d.flatten()
print("Одномерный массив:\n", array_1d)
