import pytest

numbers = [1, 3, 8, 5, 9]


def test_list_len():
    assert len(numbers) > 1


def test_list_append(list_fixture):
    numbers2 = numbers.copy()
    numbers2.append(list_fixture)
    assert numbers != numbers2


@pytest.mark.parametrize('sort', [[1, 3, 5, 8, 9]])
def test_list_sort(sort):
    numbers.sort()
    assert sort == numbers


def test_list_copy():
    numbers2 = numbers.copy()
    assert numbers == numbers2


def test_list_revers():
    before = numbers[0]
    numbers.reverse()
    after = numbers[0]
    assert before != after
