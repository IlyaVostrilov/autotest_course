# Напишите функцию, которая принимает кортеж num_tuple из 10 цифр num_tuple,
# и возвращает строку этих чисел в виде номера телефона str_phone.
# Например (Ввод --> Вывод) :
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  => "(123) 456-7890"

def create_phone_number(num_tuple):
    prefix = str('(') + str(num_tuple[0]) + str(num_tuple[1]) + str(num_tuple[2]) + ') '
    city_code = str(num_tuple[3]) + str(num_tuple[4]) + str(num_tuple[5])
    number = str('-') + str(num_tuple[6]) + str(num_tuple[7]) + str(num_tuple[8]) + str(num_tuple[9])
    str_phone = prefix + city_code + number
    return str_phone
        # Тут я пытался сделать красивее, но не получалось, как ни вертел
        # for i in num_tuple[0:3]:
        #     prefix = prefix.join(str(i))
        # for i in num_tuple[3:6]:
        #     city_code = city_code.join(str(i))
        # for i in num_tuple[6:]:
        #     number = number.join(str(i))
        # str_phone = prefix + city_code + number


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 2, 3, 0, 5, 6, 0, 8, 9, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

test_data = [
    "(123) 456-7890", "(111) 111-1111", "(023) 056-0890", "(000) 000-0000"
]


for i, d in enumerate(data):
    assert create_phone_number(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')