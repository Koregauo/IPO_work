# Ввод N с клавиатуры
N=int(input('Введите кол-во целых чисел N  '))

# Открываем файл file1_07.txt для записи
with open('file1_07.txt', 'w') as file1:
    # Ввод N целых чисел с клавиатуры и запись их в файл
    for i in range(N):
        number = int(input(f'Введите целое число '))
        file1.write(str(number) + '\n')

# Открываем файл file1_07.txt для чтения
with open('file1_07.txt', 'r') as file1:
    numbers = [int(line) for line in file1.readlines()]

    # Фильтруем четные числа
    even_numbers = [num for num in numbers if num % 2 == 0]

    # Рассчитываем среднее арифметическое четных чисел
    if even_numbers:
        sr=sum(even_numbers)/len(even_numbers)
    else:
        sr=0

# Записываем среднее арифметическое четных чисел в файл file2_07.txt
with open('file2_07.txt', 'w', encoding='utf-8') as file2:
    file2.write(f'Ср арифметическое четных чисел  {sr}')