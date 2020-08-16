import pytest

numbers = {'7', '3', '2', '6'}


def test_string_len():
    assert len(numbers) > 1


def test_string_add(sets_fixture):
    a = len(numbers)
    numbers.add(sets_fixture)
    assert len(numbers) > a


def test_string_copy():
    numbers2 = numbers.copy()
    numbers2.pop()
    assert numbers != numbers2


def test_string_clear():
    numbers2 = numbers.copy()
    numbers2.clear()
    assert numbers != numbers2


def test_string_update():
    numbers2 = numbers.copy()
    numbers2.update(range(33, 44))
    assert numbers2 != numbers

