import pytest


@pytest.mark.smoke
@pytest.mark.skip


def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "test failed because strings do not match"


def test_secondGreetCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"


@pytest.fixture()
def setup():
    print("i will be executing first")
    yield
    print("i will execute at last")


def test_fixtureDemo(setup):
    print("i will execute steps in fixtureDemo")
