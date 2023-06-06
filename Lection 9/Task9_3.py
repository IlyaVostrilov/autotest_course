# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open('test_file/task_3.txt', 'r', encoding='utf-8') as file:
    purchases = file.readlines()
    clean_purchases = list()
    purchase = 0
    for i in purchases:
        if i != '\n':
            purchase += int(i[:-1])
        else:
            clean_purchases.append(purchase)
            purchase = 0
            continue
    new_list = sorted(clean_purchases, reverse=True)
    three_most_expensive_purchases = sum(new_list[0:3])

assert three_most_expensive_purchases == 202346
