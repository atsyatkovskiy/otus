import pytest

person = {'name': 'alex', 'surname': 'kozlov', 'email': '123@ya.ru'}


def test_dict_update(dict_fixture):
    person2 = person.copy()
    person.update(dict_fixture)
    print(person)
    assert person != person2


def test_dict_len():
    a = len(person)
    assert a == 4


def test_dict_popitem():
    person2 = person.copy()
    person.popitem()
    assert person != person2


def test_dict_pop():
    person2 = person.copy()
    person.pop("name")
    print("\n", person)
    assert person != person2


def test_dict_copy():
    person2 = person.copy()
    assert person == person2

