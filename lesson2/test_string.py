import pytest

expression = 'Тестовая строка для домашнего задания'


def test_string_len():
    a = len(expression)
    assert a > 1


def test_string_count():
    a = expression.count('ы')
    assert a == 0


def test_string_isdigit():
    a = expression.isdigit()
    assert a == False


def test_string_isalpha():
    a = expression.isalpha()
    assert a == True


def test_string_split():
    a = expression.split()
    assert type(a) == list