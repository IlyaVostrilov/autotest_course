# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test1():
    assert all_division(4, 2) == 2


@pytest.mark.smoke
def test2():
    with pytest.raises(ZeroDivisionError):
        all_division(0, 0)


def test3():
    with pytest.raises(TypeError):
        all_division('a', 1)


def test4():
    assert all_division(1, 1) == 1


def test10():
    assert all_division(2, 4) == 0.5


# Команды для вызова из консоли:
# 1) Всех тестов: pytest -v
# 2) Только с маркером smoke: pytest -m smoke -v
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного: pytest -k test1 -v
