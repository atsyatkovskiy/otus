import pytest

numbers = {'7', '3', '2', '6'}


def test_sets_len():
    assert len(numbers) > 1


def test_sets_add(sets_fixture):
    a = len(numbers)
    numbers.add(sets_fixture)
    assert "hello" in numbers
    assert len(numbers) > a


def test_sets_pop():
    numbers2 = numbers.copy()
    numbers2.pop()
    assert len(numbers) != len(numbers2)
    assert numbers != numbers2


def test_sets_clear():
    numbers2 = numbers.copy()
    numbers2.clear()
    assert len(numbers) != len(numbers2)
    assert numbers != numbers2


def test_sets_update():
    numbers2 = numbers.copy()
    numbers2.update(range(33, 44))
    assert len(numbers) != len(numbers2)
    assert numbers2 != numbers

