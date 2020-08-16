import pytest

expression = 'Тестовая строка для домашнего задания'


def test_string_len():
    a = len(expression)
    assert a > 1


@pytest.mark.parametrize('missing_symbol', ['s', 'ы', '!', 'W'])
def test_string_count(missing_symbol):
    a = expression.count(missing_symbol)
    assert a == 0


def test_string_isdigit():
    a = expression.isdigit()
    assert a == False


def test_string_upper():
    a = 'hello'
    assert a.upper() == 'HELLO'


def test_string_split():
    a = expression.split()
    assert a[0] == 'Тестовая'