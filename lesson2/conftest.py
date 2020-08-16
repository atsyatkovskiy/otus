import pytest


# --fixtures
@pytest.fixture(params=[{'city': 'Moscow'}, {'book': 'test1', 'animal': 'cat'}])
def dict_fixture(request):
    return request.param


@pytest.fixture(params=[[1, 2, 3], [3 , 4, 5]])
def list_fixture(request):
    return request.param


@pytest.fixture
def string_fixture():
    print("\n===> Это фикстура 'first_fixture'")
    return


@pytest.fixture(params=[22, 33, 44])
def sets_fixture(request):
    return request.param
