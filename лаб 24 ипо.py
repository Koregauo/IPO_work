import numpy as np
def balance_array_np(N):
    # Создаем одномерный массив с рандомными числовыми значениями
    arr = np.random.randint(-100, 100, N)
    print("Первоначальный массив ", arr)

    # Подсчитываем количество положительных и отрицательных элементов
    pos_count = np.sum(arr > 0)
    neg_count = np.sum(arr < 0)

    # Определяем, какое значение (положительное или отрицательное) нужно добавить
    value_to_add = 1 if pos_count < neg_count else -1

    # Вычисляем количество элементов, которые нужно добавить
    count_to_add = abs(pos_count - neg_count)

    # Добавляем необходимое количество элементов
    arr = np.append(arr, [value_to_add] * count_to_add)

    print("Конечный массив ", arr)

# Вызываем функцию с N, введенным пользователем
balance_array_np(int(input("Введите N  ")))