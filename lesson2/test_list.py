import pytest

numbers = [1, 3, 8, 5, 9]


def test_list_len():
    assert len(numbers) > 1


def test_list_append(list_fixture):
    numbers2 = numbers.copy()
    numbers2.append(list_fixture)
    assert numbers != numbers2


def test_list_sort():
    numbers2 = numbers.copy()
    numbers2.sort()
    assert numbers != numbers2


def test_list_copy():
    numbers2 = numbers.copy()
    assert numbers == numbers2


def test_list_revers():
    numbers2 = numbers.copy()
    numbers2.reverse()
    assert numbers != numbers2