import pytest


# --fixtures
@pytest.fixture(params=[{'city': 'Moscow'}, {'book': 'test1', 'animal': 'cat'}])
def dict_fixture(request):
    return request.param


@pytest.fixture(params=[[1, 2, 3], [3, 4, 5]])
def list_fixture(request):
    return request.param


@pytest.fixture(params=[1, 3, 5, 8, 9])
def list_fixture_sort(request):
    return request.param


@pytest.fixture(params="'Строка с заглавной буквы'")
def string_fixture(request):
    print("Строка с заглавной буквы")
    return request.param


@pytest.fixture(params=["hello", 33, 44])
def sets_fixture(request):
    return request.param
