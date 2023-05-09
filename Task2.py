# Задание 1. Дано 1 число - сторона квадрата.
# Напишите программу, которая рассчитает 3 значения:
# периметр квадрата, площадь квадрата и диагональ квадрата.
side = int()
perimeter = 4*side
area = side**2
diagonal = 2**(1/2)*side
print(f'Петиметр равен {perimeter}', f'Площадь равна {area}', f'Диагональ равна {diagonal}', sep='\n')

# Задание 2. Дано квадратное уравнение x^2+bx+c=0.
# Дискриминант уравнения должен быть больше 0. Напишите программу, которая найдет
# корни квадратного уравнения и округлит их до 2 знаков после запятой.
b = float()  # параметр квадратного уравнения
c = float()  # параметр квадратного уравнения
D = b ** 2 - 4 * c  # вычисление дискриминанта
if D > 0:
    x1 = (-b + D ** (1 / 2)) / 2
    x2 = (-b - D ** (1 / 2)) / 2
    print(f'x1 = {round(x1, 2)},', f'x2 = {round (x2, 2)}')
else:
    print('Дискриминант должен быть больше 0')

# Задание 3. Дано 2 строки. Напишите программу, которая объединит эти две строки в одну и разделит
# их пробелом, а также поменяет местами первые два символа первой строки на первые
# два символа второй строки и наоборот.
str1 = input('Введите первую строку: ') + ' '
str2 = input('Введите вторую строку: ')
print(str1.replace(str1[:2], str2[:2]) + str2.replace(str2[:2], str1[:2]))

# Задание 4. Дан абсолютный путь до файла. Вывести название файла без расширения, названия диска и корневую папку.
path = r'C:\Program Files (x86)\Microsoft.NET\Primary Interop Assemblies\adodb.dll'
path = str(path.rsplit(".", 1)[0]).split("\\")  # Разделим строку на компоненты (папки и название файла без расширения)
print(f'Название файла: "{path[-1]}"', f'Название диска: "{str(path[0])}"', f'Корневая папка: "{str(path[1])}"',
      sep='\n')

# Задание 5. Дано 2 числа a и b. Используя форматирование строк, выведите на экран
# их сумму и произведение в форматах ’a + b = c’ и ’a*b = c’.
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(f'{a} + {b} = {a + b}', f'{a}*{b} = {a*b}', sep='\n')

# Задание 6. Дана строка. Напишите программу удаления символов, которые имеют нечетные значения индекса заданной строки.
string = '0123456789'
print(string[::2])

# Задание 7. Дано 2 строки из неповторяющихся символов: первая строка длиной 3 символа,
# вторая точно содержит символы первой строки в любом порядке. Напишите программу, не используя циклы и условия,
# которая находит срез минимальной длины во второй строке, который будет содержать все символы первой строки. Например,
# first_string = ‘wtf’ и second_string = ‘brick quz
# jmpy veldt whangs fox’, срез минимальной длины: ‘t whangs f’
first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'
# Найдём индексы символов из первой строки во второй
letter_index1 = second_string.find(first_string[0])
letter_index2 = second_string.find(first_string[1])
letter_index3 = second_string.find(first_string[2])
# Вычислим минимальный и максимальный индекс
min_index = min(letter_index1, letter_index2, letter_index3)
max_index = max(letter_index1, letter_index2, letter_index3)
print(second_string[min_index:max_index])
