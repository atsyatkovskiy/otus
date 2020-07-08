import pytest

@pytest.fixture
def first_fixture():
    print("\n Print 'first_fixture'")

def test_one(first_fixture):
    print("\n Run Func")
    pass

class TestFunc:

    def test_from_test_one(self, first_fixture):
        pass