# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures('start')
class TestClass:

    @pytest.mark.usefixtures('time')
    def test1(self):
        assert 1 == 1

    def test2(self):
        assert 2 == 2

