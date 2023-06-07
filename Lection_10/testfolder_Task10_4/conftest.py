import pytest
import datetime


@pytest.fixture(scope='class')
def start(request):
    request.cls.start = datetime.datetime.now()
    print(f'\nНачало выполнения тестов {request.cls.start}\n')
    yield
    request.cls.finish = datetime.datetime.now()
    print(f'\nОкончание выполнения тестов {request.cls.finish}\n')


@pytest.fixture(scope='function')
def time():
    begin = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'\nТест выполнялся {end - begin}\n')



