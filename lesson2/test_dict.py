import pytest

person = {'name': 'alex', 'surname': 'kozlov', 'email': '123@ya.ru'}


def test_dict_update(dict_fixture):
    person2 = person.copy()
    person2.update(dict_fixture)
    assert person != person2


def test_dict_get():
    assert person.get('name') == 'alex'


def test_dict_len():
    a = len(person)
    count = 0
    for x in person:
        count += 1
    assert a == count


def test_dict_popitem():
    person2 = person.copy()
    person2.popitem()
    print("\n", person2)
    assert person != person2


def test_dict_pop():
    a = len(person)
    person2 = person.copy()
    person2.pop('name')
    b = len(person2)
    assert a > b
    assert person != person2


def test_dict_copy():
    person2 = person.copy()
    assert person == person2

