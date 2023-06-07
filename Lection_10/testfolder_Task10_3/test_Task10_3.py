# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest
from contextlib import contextmanager


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@contextmanager
def no_exception():
    yield


@pytest.mark.parametrize('a,b,result', [
    pytest.param(4, 2, no_exception(), marks=pytest.mark.smoke),
    (0, 0, pytest.raises(ZeroDivisionError)),
    ('a', 1, pytest.raises(TypeError)),
    pytest.param(1, 1, no_exception(), marks=pytest.mark.skip('skipped test')),
    (2, 4, no_exception())
])
def test_division(a, b, result):
    with result:
        assert (a / b) is not None

