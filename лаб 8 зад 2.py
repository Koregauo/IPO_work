a={1, 2, 3, 4, 5, 6, 7 ,8}#множество 1
b={3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}#множество 2
numbers=a.union(b)#все различные числа
print(numbers)#выводим
nach=a.intersection(b)#находим пересечение
konech=sorted(nach)#сортируем по возратсанию
print(konech)#выводим